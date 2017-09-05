#!/usr/bin/env python

from anaTp import *
from variableDictionaries_cfi import *
from fom_ABCDRegions_cfi import *
from regionsABCD import *
import ROOT as rt
from round20 import *

def doFOM(cutList, useQCDMC = True):

    sampleType = 'Nominal'
    Wts = 'Wts'
    SigWts = 'SigWts'
    output = True 
    jetType = '3p0'
    QCDType = 'HT'
   
    for cut in cutList:
        outTableName = 'fomFiles/29Aug17/eventsABCD_FOM_'+QCDType+'_'+cut+'_29Aug17.txt' 
        outFileName = 'histFiles/29Aug17/fullSelection_'+QCDType+'_'+cut+'_29Aug17.root'
        isRegionA_FOM['mtprimeDummyA']['Cuts'] = cutsRegionA['Base'] + '&&' + cutList[cut] 
        isRegionB_FOM['mtprimeDummy']['Cuts'] = cutsRegionB['Base'] + '&&' + cutList[cut] 
        isRegionC_FOM['mtprimeDummyC']['Cuts'] = cutsRegionC['Base'] + '&&' + cutList[cut] 
        isRegionD_FOM['mtprime']['Cuts'] = cutsRegionD['Base'] + '&&' + cutList[cut]
        if 'HT' in QCDType:
            isRegionA_FOM['mtprimeDummyA']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
            isRegionB_FOM['mtprimeDummy']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
            isRegionC_FOM['mtprimeDummyC']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
            isRegionD_FOM['mtprime']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)'
            
        cutA, cutB, cutC, cutFOM = ABCD(isRegionA_FOM, isRegionB_FOM, isRegionC_FOM, isRegionD_FOM, output, outFileName, Wts, SigWts, sampleType, jetType, QCDType)

        sigFOM = {}
        sigEffFOM = {}
        sigEffFOMErr = {}
        errTmp = {}
        bkgrFOM = rt.Double(0.)
        bkgrFOMErr = rt.Double(0.)
        bkgrDataFOM = rt.Double(0.)

        bkgrFOMErrSum = rt.Double(0.)
        bkgrDataFOMErrSum = rt.Double(0.)

        estQCDErr = makeTables(cutA,cutB,cutC,cutFOM,outTableName)
        for var in cutFOM:
            for sample in cutFOM[var]:
                if 'Ttt' in sample or 'Tbt' in sample:
                    sigFOM[sample] = (cutFOM[var][sample].Integral(0,1000)/(lumi*sampleXsec[sample])) * nEvts[sample]
                    sigEffFOM[sample] = cutFOM[var][sample].Integral(0,1000)/(lumi*sampleXsec[sample])
                    sigEffFOMErr[sample] = (1/nEvts[sample])*rt.TMath.Sqrt(sigFOM[sample]*(1-(sigFOM[sample]/nEvts[sample])))
                elif 'est' in sample:
                    bkgrDataFOM += cutFOM[var][sample].Integral(0,1000)
                    bkgrDataFOMErrSum += estQCDErr*estQCDErr
                elif 'QCD' in sample and 'data' not in sample and 'est' not in sample:
                    errTmp[sample] = rt.Double(0.)
                    bkgrFOM += cutFOM[var][sample].IntegralAndError(0,1000,errTmp[sample])
                    bkgrFOMErrSum += errTmp[sample]*errTmp[sample]
                elif 'Data' not in sample and 'data' not in sample:
                    errTmp[sample] = rt.Double(0.)
                    bkgrFOM += cutFOM[var][sample].IntegralAndError(0,1000,errTmp[sample])
                    bkgrDataFOM += cutFOM[var][sample].Integral(0,1000)
                    bkgrFOMErrSum += errTmp[sample]*errTmp[sample]
                    bkgrDataFOMErrSum += errTmp[sample]*errTmp[sample]
       
        MC_FOM = {}
        MC_FOMErr = {}
        Est_FOM = {}
        Est_FOMErr = {}
        MC_RoundFOM = {}
        MC_RoundFOMErr = {}
        Est_RoundFOM = {}
        Est_RoundFOMErr = {}

        print 'bkgrFOMErrSum: ', bkgrFOMErrSum
        print 'bkgrDataFOMErrSum: ', bkgrDataFOMErrSum
  
        bkgrFOMErr = rt.TMath.Sqrt(bkgrFOMErrSum)
        bkgrDataFOMErr = rt.TMath.Sqrt(bkgrDataFOMErrSum)
        print 'bkgrFOMErr: ', bkgrFOMErr
        print 'bkgrDataFOMErr: ', bkgrDataFOMErr

        sigDiff = 1 / (2.5+rt.TMath.Sqrt(bkgrFOM))
        sigDataDiff = 1 / (2.5+rt.TMath.Sqrt(bkgrDataFOM))
        
        for signal in sigFOM:
            MC_FOM[signal] = sigEffFOM[signal] / (2.5+rt.TMath.Sqrt(bkgrFOM))
            Est_FOM[signal] = sigEffFOM[signal] / (2.5+rt.TMath.Sqrt(bkgrDataFOM))
            
            bkgrDiff = -(1/2) * sigEffFOM[signal] * (2.5+rt.TMath.Sqrt(bkgrFOM))**(-2) * bkgrFOM**(-1/2)
            bkgrDataDiff = -(1/2) * sigEffFOM[signal] * (2.5+rt.TMath.Sqrt(bkgrDataFOM))**(-2) * bkgrDataFOM**(-1/2)

            MC_FOMErr[signal] = rt.TMath.Sqrt(sigEffFOMErr[signal]**2 * sigDiff**2 + bkgrFOMErr**2 * bkgrDiff**2)
            Est_FOMErr[signal] = rt.TMath.Sqrt(sigEffFOMErr[signal]**2 * sigDataDiff**2 + bkgrDataFOMErr**2 * bkgrDataDiff**2)

            valueMC = MC_FOM[signal]
            errMC = MC_FOMErr[signal]
            valueEst = Est_FOM[signal]
            errEst = Est_FOMErr[signal]

            MC_RoundFOM[signal], MC_RoundFOMErr[signal] = roundOffErr(valueMC, errMC)
            Est_RoundFOM[signal], Est_RoundFOMErr[signal] = roundOffErr(valueEst, errEst)
        with open(outTableName, 'a') as f:
            f.write( '\n'+ 'eff/(2.5+Sqrt(B)) for signal mass points: ')
            f.write('\n Raw:')
            f.write( '\n'+'Usinge QCD MC:')
            for signal in sigFOM:
                f.write( '\n'+ signal+': '+str(MC_FOM[signal]) + ' \pm ' + str(MC_FOMErr[signal]))
            f.write('\n\n'+'Using estimated QCD:')
            for signal in sigFOM:
                f.write( '\n'+ signal+': '+str(Est_FOM[signal]) + ' \pm ' + str(Est_FOMErr[signal])) 
            f.write('\n Rounded:')
            f.write( '\n'+'Usinge QCD MC:')
            for signal in sigFOM:
                f.write( '\n'+ signal+': '+str(MC_RoundFOM[signal]) + ' \pm ' + str(MC_RoundFOMErr[signal]))
            f.write('\n\n'+'Using estimated QCD:')
            for signal in sigFOM:
                f.write( '\n'+ signal+': '+str(Est_RoundFOM[signal]) + ' \pm ' + str(Est_RoundFOMErr[signal])) 
            f.close()

if __name__ == '__main__':

    doFOM(additionalCuts) 
