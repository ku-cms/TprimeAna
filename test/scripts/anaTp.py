#!/usr/bin/env python
# this is currently a python code write up, to be fixed after overall setup is determined

import ROOT as rt
import tdrstyle
import help
import CMS_lumi
from itertools import chain
# list of root files given as Signal, Background, Data.
from input_anaTp_cfi import Signals, Backgrounds, Data, lumi, preselDict, sampleXsec
# dictionaries should take the form of 
#   {'sampleName' : file}
# sampleXsec should be a dictionary of what each histogram should be scaled to
# {'sampleName' : sampleXsection}
# also contains dictionary of variables to run through the code, each variable has a sub dictionary for cuts and weights to be applied, along with histogram variables
# dictionaries for each variable should take the form of
# { 'variableName' : { 'Wts': weight, 'Cuts' : cuts, 'histVars' : values, ...}, ...} 

def getFiles(sampleList):
    """
    Books TFiles for given list of root files
    @sampleList : [[sampleName,fileName]]
    """

    TFileList = {}
    for sample in sampleList:
        TFileList[sample] = rt.TFile(sampleList[sample],'READ')
    return TFileList


def analysis(outFileName,treeVarDict):
    """
    Takes tree variables and produces histograms normalized to sigma*lumi/nEvts
    @treeVarList : list of variables to be run through analysis
                   [name, histogram settings]
    """

    sigFiles  = getFiles(Signals)
    bkgrFiles = getFiles(Backgrounds)
    #dataFiles = getFiles(Data)

    rt.TH1.SetDefaultSumw2()

    bkgrTrees = {}
    sigTrees  = {}
    dataTree = {}

    nEvts = {}
    nEvts['ST'] = 0
    tempHists = {}

    varHists = {}

    dataTree['Data'] = rt.TChain("ana/tree")
    bkgrTrees['ST'] = rt.TChain("ana/tree")

    print "Files included:"

    for key in Signals:  
        sigTrees[key] = rt.TChain("ana/tree")
        sigTrees[key].Add(Signals[key])
        print key

    for key in Backgrounds:
        if 'ST' in key:
            bkgrTrees['ST'].Add(Backgrounds[key])
        else: 
            bkgrTrees[key] = rt.TChain("ana/tree")
            bkgrTrees[key].Add(Backgrounds[key])
        print key

    for key in Data:
        dataTree['Data'].Add(Data[key])
        print key

    for key in bkgrFiles:
        if 'ST' in key:
            tempHists[key] = bkgrFiles[key].Get("allEvents/hEventCount_wt")
            nEvts['ST'] += tempHists[key].Integral(0,10000)
        else:
            tempHists[key] = bkgrFiles[key].Get("allEvents/hEventCount_wt")
            nEvts[key] = tempHists[key].Integral(0,10000)

    for key in sigFiles:
        tempHists[key] = sigFiles[key].Get("allEvents/hEventCount_wt")
        nEvts[key] = tempHists[key].Integral(0,10000)
        
    for treeVar in treeVarDict:

        bkgrHists = {}
        sigHists = {}
        dataHist = {}

        varHists[treeVar] = None 
        print 'Retrieving histograms for: ', treeVar, ', ' + treeVarDict[treeVar]['Cuts']
        print 'Weights applied: ', treeVarDict[treeVar]['Wts']

        for key, tree in chain(sigTrees.items(),bkgrTrees.items(),dataTree.items()):
            if 'Data' in key:
                dataHist['Data'] = rt.TH1D("hData","",treeVarDict[treeVar]['nBins'],treeVarDict[treeVar]['xMin'],treeVarDict[treeVar]['xMax'])
                tree.Draw(treeVar+'>>hData',treeVarDict[treeVar]['Cuts'])
                print key + ' retrieved'
                dataHist['Data'].SetBinErrorOption(rt.TH1.kPoisson)
            else: 
                if ('LH' or 'RH') in key:
                    sigHists[key] = rt.TH1D("h"+key,"",treeVarDict[treeVar]['nBins'],treeVarDict[treeVar]['xMin'],treeVarDict[treeVar]['xMax'])
                    tree.Draw(treeVar+'>>h'+key,treeVarDict[treeVar]['Wts']+"*("+treeVarDict[treeVar]['Cuts']+")")
                    print treeVarDict[treeVar]['Wts']+"*("+treeVarDict[treeVar]['Cuts']+")"
                    print key + ' retrieved'
                else:
                    bkgrHists[key] = rt.TH1D("h"+key,"",treeVarDict[treeVar]['nBins'],treeVarDict[treeVar]['xMin'],treeVarDict[treeVar]['xMax'])
                    tree.Draw(treeVar+'>>h'+key,treeVarDict[treeVar]['Wts']+"*("+treeVarDict[treeVar]['Cuts']+")")
                    print key + ' retrieved'

        for key in sigHists:
            sigHists[key] = rt.gROOT.FindObject('h'+key)
            sigHists[key].Scale((sampleXsec[key]/nEvts[key])*lumi)

        for key in bkgrHists:
            bkgrHists[key] = rt.gROOT.FindObject('h'+key)
            bkgrHists[key].Scale((sampleXsec[key]/nEvts[key])*lumi)

        for key in dataHist:
            dataHist[key] = rt.gROOT.FindObject('h'+key)
        
        bkgrHists['QCD'] = rt.gROOT.FindObject('hQCDHT700').Clone('hQCD')
        bkgrHists.pop('QCDHT700', None)
        for key, hist in bkgrHists.items():
            if ('QCDHT' in key) and not ('700' in key):
                bkgrHists['QCD'].Add(hist)
                bkgrHists.pop(key, None)
            else:
                continue
       
        varHists[treeVar] = dataHist
        varHists[treeVar].update(bkgrHists)
        varHists[treeVar].update(sigHists)
        print 'Number of events for ' + treeVar + ':'
        for key in varHists[treeVar]:
            print varHists[treeVar][key].Integral(0,1000), ', ' + key

        dataHist.clear()
        bkgrHists.clear()
        sigHists.clear()

    outFile = rt.TFile(outFileName, "recreate")
    for key in varHists:
        dir = outFile.mkdir(key,key)
        dir.cd()
        for keyHists in varHists[key]:
            varHists[key][keyHists].Write()
        outFile.cd()
    outFile.Close()
    return varHists


def ABCD(abcdHists):
    """
    Function to calculate the numbers associated with the ABCD regions
    @abcdHists : dictionary from analysis() function containing histograms for all samples for each region
    """

if __name__ == "__main__":
    analysis('./test.root',preselDict) 
