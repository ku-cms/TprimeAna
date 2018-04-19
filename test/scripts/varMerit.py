#!/usr/bin/env python

from anaTp import *
from fom_ABCDRegions_cfi import *
from regionsABCD import *
import ROOT as rt
from round20 import *

def evaluateZbi((Nsig), (Nbkg),(sys)):
    Nobs = rt.Double(Nsig+Nbkg)
    tau = rt.Double(1./Nbkg/(sys*sys/10000.))
    aux = rt.Double(Nbkg*tau)
    Pvalue = rt.TMath.BetaIncomplete(1./(1.+tau),Nobs,aux+1.)
    return rt.TMath.Sqrt(2.)*rt.TMath.ErfcInverse(Pvalue*2)

def evaluateZapp((Nsig), (Nbkg), (sys)):
    return rt.Double(Nsig / rt.TMath.Sqrt((sys*sys/10000.)*Nbkg*Nbkg+Nbkg))

def doFOM(cutList, useQCDMC = True):

    sampleType = 'Nominal'
    Wts = 'Wts'
    SigWts = 'SigWts'
    output = True 
    jetType = 'CHS'
    QCDType = 'Pt'
    sigType = 'H'
    is2015 = False
    syst = 0.0
    doubleRatioFile = './fomFiles/doubleRatioNums_CHS_cfg.py' 
    with open(doubleRatioFile,'w') as doub:
        doub.write('doubleRatioNums = { \n')
        doub.close()
    for cut in cutList:
        outTableName = 'fomFiles/5Apr18/eventsABCD_FOM_'+QCDType+'_'+cut+'_'+jetType+'_5Apr18.txt' 
        outFileName = 'histFiles/5Apr18/fullSelection_'+QCDType+'_'+cut+'_'+jetType+'_5Apr18.root'
        with open(doubleRatioFile,'a') as doub:
            doub.write('\''+outTableName.split('/')[2].split('.')[0]+'\' : { \n')
            doub.close()
        if sigType is 'H':
            if not is2015:
                #if '800MassRegion' in cut:
                #    isRegionA_FOM['mtprimeATilde_tM_H1M0L']['Cuts'] = cutsRegionA['800MassRegion'] + cutList[cut] 
                #    isRegionB_FOM['mtprimeBTilde_tM_H1M0L']['Cuts'] = cutsRegionB['800MassRegion'] + cutList[cut] 
                #    isRegionC_FOM['mtprimeCTilde_tM_H1M0L']['Cuts'] = cutsRegionC['800MassRegion'] + cutList[cut] 
                #    isRegionD_FOM['mtprimeDTilde_tM_H1M0L']['Cuts'] = cutsRegionD['800MassRegion'] + cutList[cut]
                #elif '900MassRegion' in cut:
                #    isRegionA_FOM['mtprimeATilde_tM_H1M0L']['Cuts'] = cutsRegionA['900MassRegion'] + cutList[cut] 
                #    isRegionB_FOM['mtprimeBTilde_tM_H1M0L']['Cuts'] = cutsRegionB['900MassRegion'] + cutList[cut] 
                #    isRegionC_FOM['mtprimeCTilde_tM_H1M0L']['Cuts'] = cutsRegionC['900MassRegion'] + cutList[cut] 
                #    isRegionD_FOM['mtprimeDTilde_tM_H1M0L']['Cuts'] = cutsRegionD['900MassRegion'] + cutList[cut]
                if '1100MassRegion' in cut:
                    isRegionA_FOM['mtprimeATilde_tM_H1M0L']['Cuts'] = cutsRegionA['1100MassRegion10p'] + cutList[cut] 
                    isRegionB_FOM['mtprimeBTilde_tM_H1M0L']['Cuts'] = cutsRegionB['1100MassRegion10p'] + cutList[cut] 
                    isRegionC_FOM['mtprimeCTilde_tM_H1M0L']['Cuts'] = cutsRegionC['1100MassRegion10p'] + cutList[cut] 
                    isRegionD_FOM['mtprimeDTilde_tM_H1M0L']['Cuts'] = cutsRegionD['1100MassRegion10p'] + cutList[cut]
                elif '1200MassRegion' in cut:
                    isRegionA_FOM['mtprimeATilde_tM_H1M0L']['Cuts'] = cutsRegionA['1200MassRegion10p'] + cutList[cut] 
                    isRegionB_FOM['mtprimeBTilde_tM_H1M0L']['Cuts'] = cutsRegionB['1200MassRegion10p'] + cutList[cut] 
                    isRegionC_FOM['mtprimeCTilde_tM_H1M0L']['Cuts'] = cutsRegionC['1200MassRegion10p'] + cutList[cut] 
                    isRegionD_FOM['mtprimeDTilde_tM_H1M0L']['Cuts'] = cutsRegionD['1200MassRegion10p'] + cutList[cut]
                elif '1800MassRegion' in cut:
                    isRegionA_FOM['mtprimeATilde_tM_H1M0L']['Cuts'] = cutsRegionA['1800MassRegion10p'] + cutList[cut] 
                    isRegionB_FOM['mtprimeBTilde_tM_H1M0L']['Cuts'] = cutsRegionB['1800MassRegion10p'] + cutList[cut] 
                    isRegionC_FOM['mtprimeCTilde_tM_H1M0L']['Cuts'] = cutsRegionC['1800MassRegion10p'] + cutList[cut] 
                    isRegionD_FOM['mtprimeDTilde_tM_H1M0L']['Cuts'] = cutsRegionD['1800MassRegion10p'] + cutList[cut]
                else:
                    isRegionA_FOM['mtprimeATilde_tM_H1M0L']['Cuts'] = cutsRegionA['Base'] + cutList[cut] 
                    isRegionB_FOM['mtprimeBTilde_tM_H1M0L']['Cuts'] = cutsRegionB['Base'] + cutList[cut]
                    
                    print isRegionB_FOM['mtprimeBTilde_tM_H1M0L']['Cuts']  
                    isRegionC_FOM['mtprimeCTilde_tM_H1M0L']['Cuts'] = cutsRegionC['Base'] + cutList[cut] 
                    isRegionD_FOM['mtprimeDTilde_tM_H1M0L']['Cuts'] = cutsRegionD['Base'] + cutList[cut]
                if 'HT' in QCDType:
                    isRegionA_FOM['mtprimeATilde_tM_H1M0L']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
                    isRegionB_FOM['mtprimeBTilde_tM_H1M0L']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
                    isRegionC_FOM['mtprimeCTilde_tM_H1M0L']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
                    isRegionD_FOM['mtprimeDTilde_tM_H1M0L']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)'
                cutA, cutB, cutC, cutFOM = ABCD(isRegionA_FOM, isRegionB_FOM, isRegionC_FOM, isRegionD_FOM, output, outFileName, Wts, SigWts, sampleType, jetType, QCDType)
            else: 
                isRegionA_FOM['ht']['Cuts'] = cutsRegionA['Base'] + cutList[cut] 
                isRegionB_FOM['ht']['Cuts'] = cutsRegionB['Base'] + cutList[cut] 
                isRegionC_FOM['ht']['Cuts'] = cutsRegionC['Base'] + cutList[cut] 
                isRegionD_FOM['ht']['Cuts'] = cutsRegionD['Base'] + cutList[cut]
                cutA, cutB, cutC, cutFOM = ABCD(isRegionA_FOM, isRegionB_FOM, isRegionC_FOM, isRegionD_FOM, output, outFileName, Wts, SigWts, sampleType, jetType, QCDType)
                
            
        elif sigType is 'Z':
            isRegionA_FOM_Z['Mjj(ptAntiZTagged,etaAntiZTagged,phiAntiZTagged,MAntiZTagged,ptAntiTopTagged,etaAntiTopTagged,phiAntiTopTagged,MAntiTopTagged)']['Cuts'] = cutsRegionA['BaseZ'] + '&&' + cutList[cut] 
            isRegionB_FOM_Z['Mjj(ptAntiZTagged,etaAntiZTagged,phiAntiZTagged,MAntiZTagged,ptTopTagged,etaTopTagged,phiTopTagged,MTopTagged)']['Cuts'] = cutsRegionB['BaseZ'] + '&&' + cutList[cut] 
            isRegionC_FOM_Z['Mjj(ptZTagged,etaZTagged,phiZTagged,MZTagged,ptAntiTopTagged,etaAntiTopTagged,phiAntiTopTagged,MAntiTopTagged)']['Cuts'] = cutsRegionC['BaseZ'] + '&&' + cutList[cut] 
            isRegionD_FOM_Z['Mjj(ptZTagged,etaZTagged,phiZTagged,MZTagged,ptTopTagged,etaTopTagged,phiTopTagged,MTopTagged)']['Cuts'] = cutsRegionD['BaseZ'] + '&&' + cutList[cut]
            if 'HT' in QCDType:
                isRegionA_FOM_Z['Mjj(ptAntiZTagged,etaAntiZTagged,phiAntiZTagged,MAntiZTagged,ptAntiTopTagged,etaAntiTopTagged,phiAntiTopTagged,MAntiTopTagged)']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
                isRegionB_FOM_Z['Mjj(ptAntiZTagged,etaAntiZTagged,phiAntiZTagged,MAntiZTagged,ptTopTagged,etaTopTagged,phiTopTagged,MTopTagged)']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
                isRegionC_FOM_Z['Mjj(ptZTagged,etaZTagged,phiZTagged,MZTagged,ptAntiTopTagged,etaAntiTopTagged,phiAntiTopTagged,MAntiTopTagged)']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)' 
                isRegionD_FOM_Z['Mjj(ptZTagged,etaZTagged,phiZTagged,MZTagged,ptTopTagged,etaTopTagged,phiTopTagged,MTopTagged)']['Wts'] += '*WeightSumPt(ptAK8[0],ptAK8[1],0)'
            cutA, cutB, cutC, cutFOM = ABCD(isRegionA_FOM_Z, isRegionB_FOM_Z, isRegionC_FOM_Z, isRegionD_FOM_Z, output, outFileName, Wts, SigWts, sampleType, jetType, QCDType)

        nSig = {}
        nSigErr = {}
        sigFOM = {}
        sigEffFOM = {}
        sigEffFOMErr = {}
        errTmp = {}
        bkgrFOM = rt.Double(0.)
        bkgrFOMErr = rt.Double(0.)
        bkgrDataFOM = rt.Double(0.)

        bkgrFOMErrSum = rt.Double(0.)
        bkgrDataFOMErrSum = rt.Double(0.)

        estQCDErr = makeTables(cutA,cutB,cutC,cutFOM,outTableName,doubleRatioFile,syst)
        for var in cutFOM:
            for sample in cutFOM[var]:
                if 'Ttt' in sample or 'Tbt' in sample or 'TpTp' in sample:
                    nSigErr[sample] = rt.Double(0.)
                    nSig[sample] = cutFOM[var][sample].IntegralAndError(1,1000,nSigErr[sample])
                    sigFOM[sample] = (cutFOM[var][sample].Integral(1,1000)/(lumi*sampleXsec[sample])) * nEvts[sample]
                    sigEffFOM[sample] = cutFOM[var][sample].Integral(1,1000)/(lumi*sampleXsec[sample])
                    sigEffFOMErr[sample] = (1/nEvts[sample])*rt.TMath.Sqrt(sigFOM[sample]*(1-(sigFOM[sample]/nEvts[sample])))
                elif 'est' in sample and 'MC' not in sample:
                    bkgrDataFOM += cutFOM[var][sample].Integral(1,1000)
                    bkgrDataFOMErrSum += estQCDErr*estQCDErr
                elif 'QCD' in sample and 'data' not in sample and 'est' not in sample:
                    errTmp[sample] = rt.Double(0.)
                    bkgrFOM += cutFOM[var][sample].IntegralAndError(1,1000,errTmp[sample])
                    bkgrFOMErrSum += errTmp[sample]*errTmp[sample]
                elif 'Data' not in sample and 'data' not in sample and 'MC' not in sample:
                    errTmp[sample] = rt.Double(0.)
                    bkgrFOM += cutFOM[var][sample].IntegralAndError(1,1000,errTmp[sample])
                    bkgrDataFOM += cutFOM[var][sample].Integral(1,1000)
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
        estZbi = {}
        estZapp = {}
        mcZbi = {}
        mcZapp = {}
        mcSB = {}
        estSB = {}
        mcSB_Err = {}
        estSB_Err = {}
        print 'bkgrFOMErrSum: ', bkgrFOMErrSum
        print 'bkgrDataFOMErrSum: ', bkgrDataFOMErrSum
  
        bkgrFOMErr = rt.TMath.Sqrt(bkgrFOMErrSum)
        bkgrDataFOMErr = rt.TMath.Sqrt(bkgrDataFOMErrSum)
        print 'bkgrFOMErr: ', bkgrFOMErr
        print 'bkgrDataFOMErr: ', bkgrDataFOMErr

        sigDiff = 1 / (2.5+rt.TMath.Sqrt(bkgrFOM))
        sigDataDiff = 1 / (2.5+rt.TMath.Sqrt(bkgrDataFOM))

        if 'forward' in cut:
            sysErr = 30
        else:
            sysErr = 20
        for signal in sigFOM:
            estZbi[signal] = evaluateZbi(nSig[signal],bkgrDataFOM,sysErr)
            estZapp[signal] = evaluateZapp(nSig[signal],bkgrDataFOM,sysErr)
            mcZbi[signal] = evaluateZbi(nSig[signal],bkgrFOM,sysErr)
            mcZapp[signal] = evaluateZapp(nSig[signal],bkgrFOM,sysErr)
            mcSB[signal] = nSig[signal] / bkgrFOM
            estSB[signal] = nSig[signal] / bkgrDataFOM
            if nSig[signal] == 0: 
                mcSB_Err[signal] = 0.0
                estSB_Err[signal] = 0.0
            elif nSig[signal] > 0:
                mcSB_Err[signal] = rt.TMath.Sqrt((nSigErr[signal] / nSig[signal])**2 + (bkgrFOMErr / bkgrFOM)**2)*mcSB[signal]
                estSB_Err[signal] = rt.TMath.Sqrt((nSigErr[signal] / nSig[signal])**2 + (bkgrDataFOMErr / bkgrDataFOM)**2)*mcSB[signal]
            
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
            
            #MC_RoundFOM[signal], MC_RoundFOMErr[signal] = roundOffErr(valueMC, errMC)
            #Est_RoundFOM[signal], Est_RoundFOMErr[signal] = roundOffErr(valueEst, errEst)
        with open(outTableName, 'a') as f:
            f.write( '\n'+ 'S/B for signal mass points: ')
            f.write( '\n'+'Usinge QCD MC:')
            for signal in sorted(sigFOM):
                f.write( '\n'+ signal+': '+str(mcSB[signal]) + ' \pm ' + str(mcSB_Err[signal]))
            f.write('\n\n'+'Using estimated QCD:')
            for signal in sorted(sigFOM):
                f.write( '\n'+ signal+': '+str(estSB[signal]) + ' \pm ' + str(estSB_Err[signal]))
            f.write( '\n'+ 'Z binomial for signal mass points: ')
            f.write( '\n'+'Usinge QCD MC:')
            for signal in sorted(sigFOM):
                f.write( '\n'+ signal+': '+str(mcZbi[signal]))
            f.write('\n\n'+'Using estimated QCD:')
            for signal in sorted(sigFOM):
                f.write( '\n'+ signal+': '+str(estZbi[signal]))
            f.write( '\n\n'+ 'Z approx. for signal mass points: ')
            f.write( '\n'+'Usinge QCD MC:')
            for signal in sorted(sigFOM):
                f.write( '\n'+ signal+': '+str(mcZapp[signal]))
            f.write('\n\n'+'Using estimated QCD:')
            for signal in sorted(sigFOM):
                f.write( '\n'+ signal+': '+str(estZapp[signal]))
#            f.write( '\n\n'+ 'eff/(2.5+Sqrt(B)) for signal mass points: ')
#            f.write('\n Raw:')
#            f.write( '\n'+'Usinge QCD MC:')
#            for signal in sorted(sigFOM):
#                f.write( '\n'+ signal+': '+str(MC_FOM[signal]) + ' \pm ' + str(MC_FOMErr[signal]))
#            f.write('\n\n'+'Using estimated QCD:')
#            for signal in sorted(sigFOM):
#                f.write( '\n'+ signal+': '+str(Est_FOM[signal]) + ' \pm ' + str(Est_FOMErr[signal])) 
#            f.write('\n Rounded:')
#            f.write( '\n'+'Usinge QCD MC:')
#            for signal in sorted(sigFOM):
#                f.write( '\n'+ signal+': '+str(MC_RoundFOM[signal]) + ' \pm ' + str(MC_RoundFOMErr[signal]))
#            f.write('\n\n'+'Using estimated QCD:')
#            for signal in sorted(sigFOM):
#                f.write( '\n'+ signal+': '+str(Est_RoundFOM[signal]) + ' \pm ' + str(Est_RoundFOMErr[signal])) 
            f.close()
    with open(doubleRatioFile,'a') as doub:
        doub.write('}\n')
        doub.close()
    
if __name__ == '__main__':

    doFOM(additionalCuts) 
