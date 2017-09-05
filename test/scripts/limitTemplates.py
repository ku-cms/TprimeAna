#!/usr/bin/env python
import sys,imp
import ROOT as rt
from input_anaTp_cfi import *
from anaTp import *
from ABCDRegions_cfi import *

helper = imp.load_source('fix' , './help.py')

outFileName = sys.argv[1]
finalHists = {}
finalHists['A'] = {}
finalHists['B'] = {}
finalHists['C'] = {}
finalHists['D'] = {}

hists = {}
hists['A'] = {}
hists['B'] = {}
hists['C'] = {}
hists['D'] = {}
hists['A']['Nominal'], hists['B']['Nominal'], hists['C']['Nominal'], hists['D']['Nominal'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MTNominal.root')
#hists['A']['HTUp'], hists['B']['HTUp'], hists['C']['HTUp'], hists['D']['HTUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_HTUp.root', 'Wts_HTUp', 'SigWts_HTUp')
#hists['A']['HTDown'], hists['B']['HTDown'], hists['C']['HTDown'], hists['D']['HTDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_HTDown.root', 'Wts_HTDown', 'SigWts_HTDown')
#hists['A']['JERUp'], hists['B']['JERUp'], hists['C']['JERUp'], hists['D']['JERUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_JERUp.root', 'Wts', 'SigWts', 'JERUp')
#hists['A']['JERDown'], hists['B']['JERDown'], hists['C']['JERDown'], hists['D']['JERDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_JERDown.root', 'Wts', 'SigWts', 'JERDown')
#hists['A']['JESUp'], hists['B']['JESUp'], hists['C']['JESUp'], hists['D']['JESUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_JESUp.root', 'Wts', 'SigWts', 'JESUp')
#hists['A']['JESDown'], hists['B']['JESDown'], hists['C']['JESDown'], hists['D']['JESDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_JESDown.root', 'Wts', 'SigWts', 'JESDown')
#hists['A']['murDown'], hists['B']['murDown'], hists['C']['murDown'], hists['D']['murDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_murDown.root', 'Wts_murDown', 'SigWts_murDown')
#hists['A']['murUp'], hists['B']['murUp'], hists['C']['murUp'], hists['D']['murUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_murUp.root', 'Wts_murUp', 'SigWts_murUp')
#hists['A']['mufDown'], hists['B']['mufDown'], hists['C']['mufDown'], hists['D']['mufDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_mufDown.root', 'Wts_mufDown', 'SigWts_mufDown')
#hists['A']['mufUp'], hists['B']['mufUp'], hists['C']['mufUp'], hists['D']['mufUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_mufUp.root', 'Wts_mufUp', 'SigWts_mufUp')
#hists['A']['ttagDown'], hists['B']['ttagDown'], hists['C']['ttagDown'], hists['D']['ttagDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_ttagDown.root', 'Wts_topSFDown', 'SigWts_topSFDown')
#hists['A']['ttagUp'], hists['B']['ttagUp'], hists['C']['ttagUp'], hists['D']['ttagUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MT_ttagUp.root', 'Wts_topSFUp', 'SigWts_topSFUp')
#hists['A']['lDown'], hists['B']['lDown'], hists['C']['lDown'], hists['D']['lDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MTlDown.root', 'Wts_lDown', 'SigWts_lDown')
#hists['A']['lup'], hists['B']['lup'], hists['C']['lup'], hists['D']['lup'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MTlUp.root', 'Wts_lUp', 'SigWts_lUp')
#hists['A']['bcDown'], hists['B']['bcDown'], hists['C']['bcDown'], hists['D']['bcDown'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MTbcDown.root', 'Wts_bcDown', 'SigWts_bcDown')
#hists['A']['bcUp'], hists['B']['bcUp'], hists['C']['bcUp'], hists['D']['bcUp'] = ABCD(isRegionA_mt,isRegionB_mt,isRegionC_mt,isRegionD_mt, False, './limits/LimitHists-MTbcUp.root', 'Wts_bcUp', 'SigWts_bcUp')


for region in hists:
    print 'Region ', region
    for key in hists[region]:   
        for var in hists[region][key]:
            print 'var: ', var
            if 'D' in region:
                hists[region][key][var]['MC_QCD'] = hists[region][key][var]['QCD'].Clone('MC_QCD')
                hists[region][key][var]['QCD'] = hists[region][key][var]['dataQCD'].Clone('QCD')
                hists[region][key][var].pop('dataQCD',None)
            else:
                hists[region][key][var]['MC_QCD'] = hists[region][key][var]['QCD'].Clone('MC_QCD')
                hists[region][key][var]['QCD'] = hists[region][key][var]['dataQCD'].Clone('QCD')
                hists[region][key][var].pop('dataQCD',None)
            if 'ht' in var:
                for hist in hists[region][key][var]:
                    if 'Nominal' in key:
                        if 'Data' in hist:
                            finalHists[region][hist] = hists[region][key][var][hist].Clone('HT_region'+region+'_data_obs')
                            helper.fix(finalHists[region][hist])
                        else:
                            finalHists[region][hist] = hists[region][key][var][hist].Clone('HT_region'+region+'_'+hist)
                            helper.fix(finalHists[region][hist])
                            finalHists[region][hist+'_StatUp'] = finalHists[region][hist].Clone('HT_region'+region+'_'+hist+'_StatUp')
                            finalHists[region][hist+'_StatDown'] = finalHists[region][hist].Clone('HT_region'+region+'_'+hist+'_StatDown')
                            if 'MC_QCD' in hist and 'est' not in hist:
                                finalHists[region]['background'] = finalHists[region][hist].Clone('HT_region'+region+'_background')
                                finalHists[region]['background_StatUp'] = finalHists[region][hist].Clone('HT_region'+region+'_background_StatUp')
                                finalHists[region]['background_StatDown'] = finalHists[region][hist].Clone('HT_region'+region+'background_StatDown')
                    else:
                        if 'Data' in hist:
                            continue
                        finalHists[region][hist+'_'+key] = hists[region][key][var][hist].Clone('HT_region'+region+'_'+hist+'_'+key)
                        helper.fix(finalHists[region][hist+'_'+key])
                        if 'MC_QCD' in hist and 'est' not in hist:
                            finalHists[region]['background_'+key] = finalHists[region][hist+'_'+key].Clone('HT_region'+region+'_background_'+key)
    
                for hist in hists[region][key][var]:
                    if 'TTJets' in hist or 'WJets' in hist or 'ST' in hist or 'ZJets' in hist:
                        if 'Nominal' in key:
                                finalHists[region]['background_StatUp'].Add(finalHists[region][hist])
                                finalHists[region]['background_StatDown'].Add(finalHists[region][hist])
                                finalHists[region]['background'].Add(finalHists[region][hist])
                        else:
                            finalHists[region]['background_'+key].Add(finalHists[region][hist+'_'+key])
            elif 'mtprime' in var or 'Mjj' in var:
                for hist in hists[region][key][var]:
                    if 'Nominal' in key:
                        if 'Data' in hist:
                            finalHists[region][hist] = hists[region][key][var][hist].Clone('MTP_region'+region+'_data_obs')
                            helper.fix(finalHists[region][hist])
                        else:
                            finalHists[region][hist] = hists[region][key][var][hist].Clone('MTP_region'+region+'_'+hist)
                            helper.fix(finalHists[region][hist])
                            finalHists[region][hist+'_StatUp'] = finalHists[region][hist].Clone('MTP_region'+region+'_'+hist+'_StatUp')
                            finalHists[region][hist+'_StatDown'] = finalHists[region][hist].Clone('MTP_region'+region+'_'+hist+'_StatDown')
                            if 'MC_QCD' in hist and 'est' not in hist:
                                finalHists[region]['background'] = finalHists[region][hist].Clone('MTP_region'+region+'_background')
                                finalHists[region]['background_StatUp'] = finalHists[region][hist].Clone('MTP_region'+region+'_background_StatUp')
                                finalHists[region]['background_StatDown'] = finalHists[region][hist].Clone('MTP_region'+region+'_background_StatDown')
                    else:
                        if 'Data' in hist:
                            continue
                        finalHists[region][hist+'_'+key] = hists[region][key][var][hist].Clone('MTP_region'+region+'_'+hist+'_'+key)
                        helper.fix(finalHists[region][hist+'_'+key])
                        if 'MC_QCD' in hist and 'est' not in hist:
                            finalHists[region]['background_'+key] = finalHists[region][hist+'_'+key].Clone('MTP_region'+region+'_background_'+key)
    
                for hist in hists[region][key][var]:
                    if 'TTJets' in hist or 'WJets' in hist or 'ST' in hist or 'ZJets' in hist:
                        if 'Nominal' in key:
                            finalHists[region]['background_StatUp'].Add(finalHists[region][hist])
                            finalHists[region]['background_StatDown'].Add(finalHists[region][hist])
                            finalHists[region]['background'].Add(finalHists[region][hist])
                        else:
                            finalHists[region]['background_'+key].Add(finalHists[region][hist+'_'+key])

print 'Producing statistical templates'                     
statErrUpMT = {}
statErrUpMT['A'] = {}
statErrUpMT['B'] = {}
statErrUpMT['C'] = {}
statErrUpMT['D'] = {}
statErrDownMT = {}
statErrDownMT['A'] = {}
statErrDownMT['B'] = {}
statErrDownMT['C'] = {}
statErrDownMT['D'] = {}

for region in finalHists:
    for i in xrange(1,37):
        statErrUpMT[region][i-1] = finalHists[region]['QCD_StatUp'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Up')
        statErrDownMT[region][i-1] = finalHists[region]['QCD_StatDown'].Clone('MTP_region'+region+'_QCD_bin'+str(i)+'Down')
        statErrUpMT[region][i-1].SetBinContent(i,statErrUpMT[region][i-1].GetBinContent(i)+statErrUpMT[region][i-1].GetBinError(i))
        statErrDownMT[region][i-1].SetBinContent(i,statErrDownMT[region][i-1].GetBinContent(i)-statErrDownMT[region][i-1].GetBinError(i))
    
        for key in finalHists[region]:
            if 'StatUp' in key:
                finalHists[region][key].SetBinContent(i,finalHists[region][key].GetBinContent(i)+finalHists[region][key].GetBinError(i))
            elif 'StatDown' in key:
                finalHists[region][key].SetBinContent(i,finalHists[region][key].GetBinContent(i)-finalHists[region][key].GetBinError(i))

outFile = rt.TFile(outFileName, 'recreate')
for region in finalHists:
    for key in finalHists[region]:
        finalHists[region][key].Write()
    for entry in statErrUpMT[region]:
        statErrUpMT[region][entry].Write()
    for entry in statErrDownMT[region]:
        statErrDownMT[region][entry].Write()
outFile.Close()
print 'done'
