#!/usr/bin/env python:

import os, re, sys, optparse, commands, shutil, imp
import math
import ROOT as rt
from input_anaTp_cfi import *

helper   = imp.load_source('fix'     , './help.py')
tdrstyle = imp.load_source('tdrstyle', './tdrstyle.py')
CMS_lumi = imp.load_source('CMS_lumi', './CMS_lumi.py') 

def DrawPlots(fin, varDict, doData, doScale, outDir, region):

  rt.gROOT.SetBatch()
  rt.gROOT.SetStyle('Plain')
  rt.gStyle.SetOptTitle(0) 
  rt.gStyle.SetOptStat(0000) 
  rt.gStyle.SetOptFit(0111) 
  rt.gStyle.SetErrorX(0.0001)

  fin = rt.TFile(fin, 'READ')
  rt.SetOwnership(fin,True)

  bkgrHists = {}
  sigHists = {}
  dataHist = {}

  nData = rt.Double(0.)
  nBkgrTot = rt.Double(0.)
  nBkgr = {}

  for var in varDict:
    if '/' in var:
      histDir = var.split('/')[0] 
    else:
      histDir = var
        
    for bkgr in plotDictBkgrTemp:
      #bkgrHists[bkgr] = fin.Get(histDir +'/'+ bkgr)
      print bkgr
      bkgrHists[bkgr] = fin.Get(histDir +'_'+ bkgr)
      helper.fix(bkgrHists[bkgr])

    for sig in plotDictSignal:
#      sigHists[sig] = fin.Get(histDir +'/'+ sig)
#      print sig
      sigHists[sig] = fin.Get(histDir +'_'+ sig)
      helper.fix(sigHists[sig])
      if doScale:
        sigHists[sig].Scale(plotDictSignal[sig]['Scale'])
    for bkgr in bkgrHists:
      nBkgr[bkgr] = rt.Double(0.)
      nBkgr[bkgr] = bkgrHists[bkgr].Integral()
    if doData:
#      dataHist['Data'] = fin.Get(histDir + '/Data') 
      dataHist['Data'] = fin.Get(histDir + '_data_obs') 
      nData = dataHist['Data'].Integral()
      rescaleQCD = nData
      for bkgr in bkgrHists:
        if 'QCD' not in bkgr:
          rescaleQCD -= nBkgr[bkgr]
      #bkgrHists['MC_QCD'].Scale(rescaleQCD/nBkgr['MC_QCD'])
      bkgrHists['QCD'].Scale(rescaleQCD/nBkgr['QCD'])

    if '$' in histDir:
      histDir = histDir.replace('$','')
    if '@' in histDir:
      histDir = histDir.replace('@','')
    if '>' in histDir:
      histDir = histDir.replace('>','great')
    if '<' in histDir:
      histDir = histDir.replace('<','less')
    if '[' in histDir:
      histDir = histDir.replace('[','')
    if ']' in histDir:
      histDir = histDir.replace(']','')
    if '(' in histDir:
      histDir = histDir.replace('(','')
    if ')' in histDir:
      histDir = histDir.replace(')','')
    if ',' in histDir:
      histDir = histDir.replace(',','_')
    if 'idxAK8' in histDir:
      histDir = histDir.replace('idxAK8','_')
    
    histBkgr = bkgrHists['TTJets'].Clone('hbkgr')
    for bkgr in bkgrHists:
      if 'TTJets' not in bkgr:
        histBkgr.Add(bkgrHists[bkgr])
    
    if doData:
      hratio = dataHist['Data'].Clone('hratio')
      hratio.Divide(histBkgr)

      dataHist['Data'].SetMarkerStyle(20)
      dataHist['Data'].SetLineStyle(1)
      dataHist['Data'].SetLineWidth(2)
      dataHist['Data'].SetLineColor(1)

      hratio.SetMarkerStyle(20)
      hratio.SetLineStyle(1)
      hratio.SetLineWidth(2)
      hratio.SetLineColor(1)
    
    histBkgr.SetLineStyle(1)
    histBkgr.SetLineWidth(1)
    histBkgr.SetLineColor(1)
    histBkgr.SetFillColor(0)

    for bkgr in bkgrHists:
      bkgrHists[bkgr].SetLineColor(plotDictBkgrTemp[bkgr]['Color'])
      bkgrHists[bkgr].SetFillColor(plotDictBkgrTemp[bkgr]['Color'])

    for sig in sigHists:
      sigHists[sig].SetLineColor(plotDictSignal[sig]['Color'])
      sigHists[sig].SetLineWidth(2)
      sigHists[sig].SetLineStyle(1)  
      sigHists[sig].SetFillColor(0)

    stackBkgr = rt.THStack('hsbkg','')
    for bkgr, value in sorted(nBkgr.iteritems(), key=lambda (k,v): (v,k)):
      stackBkgr.Add(bkgrHists[bkgr])
      print bkgr, ' ', value

    if doData:
      c0 = rt.TCanvas('c_data_mc_'+histDir,'',800,600)
    else:
      c0 = rt.TCanvas('c_mc_'+histDir,'',800,600)

    rt.SetOwnership(c0,False)
    c0.cd()

    if doData:
      pad0 = rt.TPad("pad0","",0.0,0.3,1.0,1.0)
      pad1 = rt.TPad("pad1","",0.0,0.0,1.0,0.3)
    else:
      pad0 = rt.TPad("pad0","",0.0,0.1,1.0,1.0)

    if varDict[var]['log']:
      pad0.SetLogy()
    pad0.Draw()
    pad0.cd()
    pad0.SetBottomMargin(0.05)

    if doData:
      dataHist['Data'].GetYaxis().SetTitle(varDict[var]['yLabel'])
      dataHist['Data'].GetYaxis().SetTitleSize(0.14*0.3/0.7)
      dataHist['Data'].GetYaxis().SetTitleOffset(0.35*7/3)

      dataHist['Data'].GetXaxis().SetTitle(varDict[var]['xLabel'])
      dataHist['Data'].GetXaxis().SetTitleSize(0.14*0.3/0.7)
      dataHist['Data'].GetXaxis().SetLabelSize(0.14*0.3/0.7)
      dataHist['Data'].GetXaxis().SetTitleOffset(0.6)
    else:
      histBkgr.GetYaxis().SetTitle(varDict[var]['yLabel'])
      histBkgr.GetYaxis().SetTitleSize(0.14*0.3/0.7)
      histBkgr.GetYaxis().SetTitleOffset(0.35*7/3)

      histBkgr.GetXaxis().SetTitle(varDict[var]['xLabel'])
      histBkgr.GetXaxis().SetTitleSize(0.05)
      histBkgr.GetXaxis().SetLabelSize(0.14*0.3/0.7)
      histBkgr.GetXaxis().SetTitleOffset(1.2)
      histBkgr.GetYaxis().SetDecimals(False)
      rt.TGaxis.SetMaxDigits(3)

    if doData:
      dataHist['Data'].Draw('e1')
      stackBkgr.Draw('histsame')
    else:
      histBkgr.Draw('hist')
      stackBkgr.Draw('histsame')
    #histBkgr.Draw('e1same')
    if doData:
      dataHist['Data'].Draw('e1same')  
    for sig in sigHists:
      sigHists[sig].Draw('histsame')
   
    if doData:
      if varDict[var]['xMin'] < dataHist['Data'].GetBinLowEdge(1):
        varDict[var]['xMin'] = dataHist['Data'].GetBinLowEdge(1)
      if varDict[var]['xMax'] > dataHist['Data'].GetBinLowEdge(dataHist['Data'].GetNbinsX()) + dataHist['Data'].GetBinWidth(dataHist['Data'].GetNbinsX()): 
        varDict[var]['xMax'] = dataHist['Data'].GetBinLowEdge(dataHist['Data'].GetNbinsX()) + dataHist['Data'].GetBinWidth(dataHist['Data'].GetNbinsX())
      dataHist['Data'].GetXaxis().SetTitle(varDict[var]['xLabel'])
      dataHist['Data'].GetXaxis().SetLabelSize(0)
    pad0.RedrawAxis()
    pad0.Update()

    if doData:
      ymax = max( [dataHist['Data'].GetMaximum(), histBkgr.GetMaximum()])
    else:
      ymax = histBkgr.GetMaximum() 

    if varDict[var]['log']:
      if doData: 
        dataHist['Data'].SetMaximum(ymax*5000)
      else:
        histBkgr.SetMaximum(ymax*5000)
    else:
      if doData:
        dataHist['Data'].SetMaximum(ymax*2)
      else:
        histBkgr.SetMaximum(ymax*2)
    if doData:
      dataHist['Data'].SetMinimum(0.1)
    else:
      histBkgr.SetMinimum(0.1)

    leg = rt.TLegend(0.12,0.66,0.88,0.88,'','brNDC') 
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetTextSize(0.03)
    leg.SetMargin(0.2)
    if doData:
      leg.SetNColumns(4)
      leg.SetColumnSeparation(0.09)
      leg.SetTextSize(0.03)
    else:
      leg.SetNColumns(3)
      leg.SetColumnSeparation(0.2)
      leg.SetTextSize(0.02)

    if doData:
      leg.AddEntry(dataHist['Data'],"Data            ", "ep")
    for key, value in sorted(nBkgr.iteritems(), key=lambda (k,v): (v,k), reverse=True):
      leg.AddEntry(bkgrHists[key], plotDictBkgrTemp[key]['Legend'], "fl") 
    for sig in sorted(sigHists.iterkeys()):
      if doScale:
        leg.AddEntry(sigHists[sig], plotDictSignal[sig]['LegendScaled'], "fl")
      else: 
        leg.AddEntry(sigHists[sig], plotDictSignal[sig]['Legend'], "fl")

    leg.Draw()
    c0.cd()

    if doData:
      pad1.Draw() 
      pad1.cd()
      pad1.SetTopMargin(0.05)
      pad1.SetBottomMargin(0.4)
      dataHist['Data'].GetXaxis().SetTitleSize(0)

      hratio.GetXaxis().SetTitle(dataHist['Data'].GetXaxis().GetTitle())
      hratio.GetXaxis().SetTitleSize(0.14)
      hratio.GetXaxis().SetLabelSize(0.14)
      hratio.GetXaxis().SetTickLength(dataHist['Data'].GetYaxis().GetTickLength())
      hratio.GetXaxis().SetTitleOffset(1.20)
      hratio.GetXaxis().SetNdivisions(510)

      hratio.GetYaxis().SetTitle("Data/MC")
      hratio.GetYaxis().SetTitleSize(0.14)
      hratio.GetYaxis().SetLabelSize(0.14)
      hratio.GetYaxis().SetTickLength(dataHist['Data'].GetYaxis().GetTickLength())
      hratio.GetYaxis().SetTitleOffset(0.35)
      hratio.GetYaxis().SetNdivisions(504)
      
      hratio.Draw("e0")

      hratio.GetXaxis().SetRangeUser(rt.Double(varDict[var]['xMin']),rt.Double(varDict[var]['xMax']))
      hratio.SetMinimum(0.0)
      hratio.SetMaximum(2.0)

      line = rt.TLine(rt.Double(varDict[var]['xMin']),1.,rt.Double(varDict[var]['xMax']),1.)
      line.Draw()
      pad1.RedrawAxis()

    c0.cd()

    CMS_lumi.lumi_13TeV = "35.9/fb"
    CMS_lumi.writeExtraText = 1
    if doData:
      CMS_lumi.extraText = "Preliminary"
    else:
      CMS_lumi.extraText = "Simulation"
    iPos = 0
    if( iPos==0 ): CMS_lumi.relPosX = 0.13
    
    CMS_lumi.CMS_lumi(c0, 4, iPos, varDict[var]['log'], doData)
    c0.Update() 
    if varDict[var]['log']:
      isLog = 'log'
    else:
      isLog = 'linear'
    c0.SaveAs(outDir+'/'+c0.GetName()+'_'+isLog+region+'.pdf')    #  change date for new plots
    c0.SaveAs(outDir+'/'+c0.GetName()+'_'+isLog+region+'.png')  #  change date for new plots

 
