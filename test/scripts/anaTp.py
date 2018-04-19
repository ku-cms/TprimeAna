#!/usr/bin/env python
# this is currently a python code write up, to be fixed after overall setup is determined

import ROOT as rt
#import tdrstyle
#import help
#import CMS_lumi
from itertools import chain
import gc
from input_anaTp_cfi import *

# dictionaries should take the form of 
#   {'sampleName' : file}
# sampleXsec should be a dictionary of what each histogram should be scaled to
# {'sampleName' : sampleXsection}
# also contains dictionary of variables to run through the code, each variable has a sub dictionary for cuts and weights to be applied, along with histogram variables
# dictionaries for each variable should take the form of
# { 'variableName' : { 'Wts': weight, 'Cuts' : cuts, 'histVars' : values, ...}, ...} 

from os import path

# weightFunctions.C needs to be in the directory from which anaTp.py is run. This makes the weight functions visible
# to Cint so that they can be loaded into the TTree.Draw() method
if path.exists('weightFunctions.C'):
    rt.gROOT.Macro('weightFunctions.C')

nEvts = {}

def getFiles(sampleDict):
    '''
    Books TFiles for given list of root files
    @sampleDict : {sampleName : lfn}
    '''

    TFileList = {}
    for sample in sampleDict:
        TFileList[sample] = rt.TFile(sampleDict[sample],'READ')
    return TFileList

def analysis(treeVarDict, sample = 'Nominal', Wts = 'Wts', SigWts = 'SigWts', output = True, outFileName = './output.root', jetType = 'CHS', QCDType = 'Pt'):
    '''
    Takes tree variables and produces histograms normalized to sigma*lumi/nEvts
    @treeVarDict : dictionary of variables to be run through analysis
                   {name :  histogram settings}
    @output : boolean to to determine whether an output file is created
    @outFileName : name of the output root file containing the histograms
    '''
    rt.gROOT.SetBatch()
    if 'Nominal' in  sample:
        if 'Pt' in QCDType:
            Signals = SignalFiles['Nominal']
            Backgrounds = BackgroundFilesPt['Nominal']   
        elif 'HT' in QCDType:
            Signals = SignalFiles['Nominal']
            Backgrounds = BackgroundFilesHT['Nominal']   
    elif 'JERUp' in  sample:
        Signals = SignalFiles['JERUp']
        Backgrounds = BackgroundFiles['JERUp']   
    elif 'JERDown' in  sample:
        Signals = SignalFiles['JERDown']
        Backgrounds = BackgroundFiles['JERDown']
    elif 'JESUp' in  sample:
        Signals = SignalFiles['JESUp']
        Backgrounds = BackgroundFiles['JESUp']
    elif 'JESDown' in  sample:
        Signals = SignalFiles['JESDown']
        Backgrounds = BackgroundFiles['JESDown']
    
    sigFiles  = getFiles(Signals)
    bkgrFiles = getFiles(Backgrounds)
    #dataFiles = getFiles(Data)

    rt.TH1.SetDefaultSumw2()
    rt.TH1.AddDirectory(rt.kFALSE)
    bkgrTrees = {}
    sigTrees  = {}
    dataTree = {}

    tempHists = {}

    varHists = {}
    dataTree['Data'] = rt.TChain('anaCHS/tree')

    print 'Files included:'

    for key in Signals:  
        sigTrees[key] = rt.TChain('ana'+jetType+'/tree')
        sigTrees[key].Add(Signals[key])
        print key

    for key in Backgrounds:
        if 'ST' in key and '_t_' not in key:
            bkgrTrees['ST'] = rt.TChain('ana'+jetType+'/tree')
            bkgrTrees['ST'].Add(Backgrounds[key])
            nEvts['ST'] = 0
        else: 
            bkgrTrees[key] = rt.TChain('ana'+jetType+'/tree')
            bkgrTrees[key].Add(Backgrounds[key])
        print key

    for key in Data:
        dataTree['Data'].Add(Data[key])
        print key

    for key in bkgrFiles:
        if 'ST' in key and '_t_' not in key:
            tempHists[key] = bkgrFiles[key].Get('allEvents/hEventCount_wt')
            nEvts['ST'] += tempHists[key].Integral(1,10000)
        else:
            tempHists[key] = bkgrFiles[key].Get('allEvents/hEventCount_wt')
            nEvts[key] = tempHists[key].Integral(1,10000)

    for key in sigFiles:
        tempHists[key] = sigFiles[key].Get('allEvents/hEventCount_wt')
        nEvts[key] = tempHists[key].Integral(1,10000)
    for treeVar in treeVarDict:

        varHists[treeVar] = {} 
        print 'Retrieving histograms for: ', treeVar, ', ' + treeVarDict[treeVar]['Cuts']
        print 'Weights applied: ', treeVarDict[treeVar][Wts]

        for key, tree in chain(sigTrees.items(),bkgrTrees.items(),dataTree.items()):
            if 'Data' in key:
                tree.Draw(treeVar+'>>Data('+treeVarDict[treeVar]['nBins']+','+treeVarDict[treeVar]['xMin']+','+treeVarDict[treeVar]['xMax']+')',treeVarDict[treeVar]['Cuts'])
                varHists[treeVar]['Data'] = rt.gROOT.FindObject('Data')
                print key + ' retrieved'
                varHists[treeVar]['Data'].SetBinErrorOption(rt.TH1.kPoisson)
            else: 
                if 'LH' in key or 'RH' in key or 'TpTp' in key:
                    tree.Draw(treeVar+'>>'+key+'('+treeVarDict[treeVar]['nBins']+','+treeVarDict[treeVar]['xMin']+','+treeVarDict[treeVar]['xMax']+')',treeVarDict[treeVar][SigWts]+'*('+treeVarDict[treeVar]['Cuts']+')')
                    print key + ' retrieved'
                    varHists[treeVar][key] = rt.gROOT.FindObject(key)
                    sigFiles[key].Close()
                else:
                    if 'QCD' in key and 'lhewts.second' in treeVarDict[treeVar][Wts]:
                        if '[5]' in treeVarDict[treeVar][Wts]:
                            tree.Draw(treeVar+'>>'+key+'('+treeVarDict[treeVar]['nBins']+','+treeVarDict[treeVar]['xMin']+','+treeVarDict[treeVar]['xMax']+')',treeVarDict[treeVar][Wts].replace('*(SelectedEvent_lhewts.second[5]/SelectedEvent_lhewts.second[1])','')+'*('+treeVarDict[treeVar]['Cuts']+')')
                            #tree.Draw(treeVar+'>>'+key+'('+treeVarDict[treeVar]['nBins']+','+treeVarDict[treeVar]['xMin']+','+treeVarDict[treeVar]['xMax']+')',treeVarDict[treeVar][Wts].replace('*SelectedEvent_lhewts.second[5]','')+'*('+treeVarDict[treeVar]['Cuts']+')')
                        elif '[9]' in treeVarDict[treeVar][Wts]:
                            tree.Draw(treeVar+'>>'+key+'('+treeVarDict[treeVar]['nBins']+','+treeVarDict[treeVar]['xMin']+','+treeVarDict[treeVar]['xMax']+')',treeVarDict[treeVar][Wts].replace('*(SelectedEvent_lhewts.second[9]/SelectedEvent_lhewts.second[1])','')+'*('+treeVarDict[treeVar]['Cuts']+')')
                            #tree.Draw(treeVar+'>>'+key+'('+treeVarDict[treeVar]['nBins']+','+treeVarDict[treeVar]['xMin']+','+treeVarDict[treeVar]['xMax']+')',treeVarDict[treeVar][Wts].replace('*SelectedEvent_lhewts.second[9]','')+'*('+treeVarDict[treeVar]['Cuts']+')')
                        print 'changed weights'
                    else:
                        tree.Draw(treeVar+'>>'+key+'('+treeVarDict[treeVar]['nBins']+','+treeVarDict[treeVar]['xMin']+','+treeVarDict[treeVar]['xMax']+')',treeVarDict[treeVar][Wts]+'*('+treeVarDict[treeVar]['Cuts']+')')
                    print key + ' retrieved'
                    varHists[treeVar][key] = rt.gROOT.FindObject(key)
                    if 'ST' not in key and 'Mtt' not in key:
                        bkgrFiles[key].Close()
        for key in varHists[treeVar]:
            if 'Data' not in key:
                print key
                varHists[treeVar][key].Scale((sampleXsec[key]/nEvts[key])*lumi)
        if QCDType is 'Pt':
            varHists[treeVar]['QCD'] = varHists[treeVar]['QCDPt3200'].Clone('QCD')
            varHists[treeVar].pop('QCDPt3200', None)
            for key, hist in varHists[treeVar].items():
                if ('QCDPt' in key):
                    varHists[treeVar]['QCD'].Add(hist)
                    varHists[treeVar].pop(key, None)
                else:
                    continue
        elif QCDType is 'HT': 
            varHists[treeVar]['QCD'] = varHists[treeVar]['QCDHT700'].Clone('QCD')
            varHists[treeVar].pop('QCDHT700', None)
            for key, hist in varHists[treeVar].items():
                if ('QCDHT' in key):
                    varHists[treeVar]['QCD'].Add(hist)
                    varHists[treeVar].pop(key, None)
                else:
                    continue
        for key in varHists[treeVar]:
            if 'Mtt' in key:
                varHists[treeVar]['TTJetsMtt'] = varHists[treeVar]['TTJetsMtt700'].Clone('TTJetsMtt')
                varHists[treeVar]['TTJetsMtt'].Add(varHists[treeVar]['TTJetsMtt1000'])
                #varHists[treeVar].pop('TTJetsMtt700', None)
                #varHists[treeVar].pop('TTJetsMtt1000', None)
                break
        for key in varHists[treeVar]:
            if 'ST_t' in key:
                varHists[treeVar]['ST_t'] = varHists[treeVar]['ST_t_top'].Clone('ST_t')
                varHists[treeVar]['ST_t'].Add(varHists[treeVar]['ST_t_antitop'])
                varHists[treeVar].pop('ST_t_top', None)
                varHists[treeVar].pop('ST_t_antitop', None)
                break

        print 'Number of events for ' + treeVar + ':'
        for key in varHists[treeVar]:
            error = rt.Double(0)
            integral = varHists[treeVar][key].IntegralAndError(1,1000,error)
            print key + ':      ', integral, ' +\- ', error

    if output is True:
        outFile = rt.TFile(outFileName, 'recreate')
        for key in varHists:
            dir = outFile.mkdir(key,key)
            dir.cd()
            for keyHists in varHists[key]:
                varHists[key][keyHists].Write()
            outFile.cd()
        outFile.Close()
    return varHists

def ABCD(RegionA, RegionB, RegionC, RegionD, output = True, outFileName = './signalRegionD.root', Wts = 'Wts', SigWts = 'SigWts', sampleType = 'Nominal', jetType = 'CHS', QCDType = 'Pt'):
    '''
    Function to calculate the numbers associated with the ABCD regions
    @isRegion : variable dictionary for the different regions and their cuts
    '''
    cutA = analysis(RegionA, sampleType, Wts, SigWts, False, './dontMatterA.root', jetType, QCDType)
    cutB = analysis(RegionB, sampleType, Wts, SigWts, False, './dontMatterB.root', jetType, QCDType)
    cutC = analysis(RegionC, sampleType, Wts, SigWts, False, './dontMatterC.root', jetType, QCDType)
    cutD = analysis(RegionD, sampleType, Wts, SigWts, False, './dontMatterD.root', jetType, QCDType)
    

    for var in cutA:
        cutA[var]['dataQCD'] = cutA[var]['Data'].Clone('dataQCD')
        varA = var
        for key in cutA[var]:
            if ('Data' not in key) and ('QCD' not in key) and ('LH' not in key) and ('RH' not in key) and ('TpTp' not in key):
                cutA[var]['dataQCD'].Add(cutA[var][key],-1)
    for var in cutB:
        varB = var
        cutB[var]['dataQCD'] = cutB[var]['Data'].Clone('dataQCD')
        print 'dataQCD: ', cutB[var]['dataQCD'].Integral(1,1000)
        for key in cutB[var]:
            if ('Data' not in key) and ('QCD' not in key) and ('LH' not in key) and ('RH' not in key) and ('TpTp' not in key):
                cutB[var]['dataQCD'].Add(cutB[var][key],-1)
    for var in cutC:
        cutC[var]['dataQCD'] = cutC[var]['Data'].Clone('dataQCD')
        varC = var
        for key in cutC[var]:
            if ('Data' not in key) and ('QCD' not in key) and ('LH' not in key) and ('RH' not in key) and ('TpTp' not in key):
                cutC[var]['dataQCD'].Add(cutC[var][key],-1)
    for var in cutD:
        cutD[var]['dataQCD'] = cutD[var]['Data'].Clone('dataQCD')
        if 'mtprime' in var or 'Mjj' in var:
            cutD[var]['estQCD'] = cutB[varB]['dataQCD'].Clone('estQCD')
            cutD[var]['estQCD'].Scale(cutC[varC]['dataQCD'].Integral(1,1000)/cutA[varA]['dataQCD'].Integral(1,1000))
            cutD[var]['MC_estQCD'] = cutB[varB]['QCD'].Clone('estQCD_MC')
            cutD[var]['MC_estQCD'].Scale(cutC[varC]['QCD'].Integral(1,1000)/cutA[varA]['QCD'].Integral(1,1000))
            print 'B*C/A = ', cutB[varB]['dataQCD'].Integral(1,1000)*(cutC[varC]['dataQCD'].Integral(1,1000)/cutA[varA]['dataQCD'].Integral(1,1000))
        else:
            cutD[var]['estQCD'] = cutB[var]['dataQCD'].Clone('estQCD')
            cutD[var]['estQCD'].Scale(cutC[var]['dataQCD'].Integral(1,1000)/cutA[var]['dataQCD'].Integral(1,1000))
            print 'B*C/A = ',  cutB[var]['dataQCD'].Integral(1,1000)*(cutC[var]['dataQCD'].Integral(1,1000)/cutA[var]['dataQCD'].Integral(1,1000))
        for key in cutD[var]:
            if ('Data' not in key) and ('QCD' not in key) and ('LH' not in key) and ('RH' not in key) and ('TpTp' not in key):
                cutD[var]['dataQCD'].Add(cutD[var][key],-1)
    if output is True:
        outFile = rt.TFile(outFileName, 'recreate')
        for var in cutD:
            #dir = outFile.mkdir(var,var)
            #dir.cd()
            for hist in cutD[var]:
                cutD[var][hist].Write()
            outFile.cd()
        outFile.Close()
    gc.collect()
#    return cutD
    for var in cutC:
        print cutC[var]['dataQCD'].Integral(1,1000)
    return cutA, cutB, cutC, cutD

def Mjj(idx1, idx2):
    return 'mass(ptAK8['+str(idx1)+'],etaAK8['+str(idx1)+'],phiAK8['+str(idx1)+'],MAK8['+str(idx1)+'],ptAK8['+str(idx2)+'],etaAK8['+str(idx2)+'],phiAK8['+str(idx2)+'],MAK8['+str(idx)+'])'

if __name__ == '__main__':
    
    #analysis(preselDict, False, './test.root')
    ABCD(isRegionA,isRegionB_mt,isRegionC,isRegionD_mt, True, './limits/LimitHists-MTNominal.root')
