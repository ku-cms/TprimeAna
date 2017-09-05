#!/usr/bin/env python:

import os, re, sys, optparse, commands, shutil, imp
import math, ROOT

helper   = imp.load_source('fix'     , './help.py')
tdrstyle = imp.load_source('tdrstyle', './tdrstyle.py')
CMS_lumi = imp.load_source('CMS_lumi', './CMS_lumi.py') 

# fin = file input ( the root file )
# hist = partial name of canvas -> gets used to name output pdf and root files
# xlow, xhigh = bounds of x axis for plot
# doratiofit = bool, linear fit of data vs MC , normally false
# xLabel, yLabel = axis labels
# doLog = bool, make y axis a log scale, normally false
# doData = bool, if you are plotting "DATA" from the detector true, for MC false. 
# myDir = name of histgram directory to make plots from.

def DrawPlots(fin, hist, xlow, xhigh, doratiofit, xLabel, yLabel, doLog, doData, mydir, outDir, region): 

  ROOT.gROOT.SetBatch()
  ROOT.gROOT.SetStyle('Plain')
  ROOT.gStyle.SetOptTitle(0) 
  ROOT.gStyle.SetOptStat(0000) 
  ROOT.gStyle.SetOptFit(0111) 
  ROOT.gStyle.SetErrorX(0.0001);
  
  fin = ROOT.TFile(fin,'READ')
  ROOT.SetOwnership(fin,True)
#  if doData:
  hdata      = fin.Get( mydir + 'Data')  # change to match your file name in histogram.
  httjets    = fin.Get( mydir + 'TTJets')
  hsingletop = fin.Get( mydir + 'ST')
  hwjets     = fin.Get( mydir + 'WJets')
  hqcd       = fin.Get( mydir + 'QCD')
  httw       = fin.Get( mydir + 'ttWJets')
  httz       = fin.Get( mydir + 'ttZJets')
  #hthq       = fin.Get( mydir + 'THQ')
  #hdy       = fin.Get( mydir + 'DYJets')
  htp1000LH    = fin.Get( mydir + 'TbtH_1800_LH') # mass point plotted
  htp1200LH    = fin.Get( mydir + 'TbtH_1200_LH') # mass point plotted
  #htp1500LH    = fin.Get(mydir + 'TttH_1200_RH')
  #htp1800LH    = fin.Get(mydir +'TttH_1800_RH')


  helper.fix(hdata     )
  helper.fix(httjets   )
  helper.fix(hsingletop)
  helper.fix(hwjets    )
  helper.fix(hqcd      )
  helper.fix(httw      )
  helper.fix(httz      )
  #helper.fix(hthq      )
  #helper.fix(hdy      )
  helper.fix(htp1000LH )
  helper.fix(htp1200LH )
  #helper.fix(htp1500LH )
  #helper.fix(htp1800LH )

  if doData:
    ndata      = hdata.Integral() 
    nttjets    = httjets.Integral() 
    nsingletop = hsingletop.Integral() 
    nwjets     = hwjets.Integral() 
    nqcd       = hqcd.Integral() 
    nttw       = httw.Integral() 
    nttz       = httz.Integral() 
#    nthq       = hthq.Integral() 
#    ndy        = hdy.Integral() 
    #rescalescd = ndata - nttjets - nwjets - nsingletop - nttw - nttz - nthq - ndy
    rescalescd = ndata - nttjets - nwjets - nsingletop - nttw - nttz
    hqcd.Scale(rescalescd/nqcd)
  scale = 1
  if doLog:
    scale = 1
 # elif 'A' in region:
 #   scale = 10000
 # elif 'B' in region:
 #   scale = 100
 # elif 'C' in region:
 #   scale = 100
 # elif 'D' in region:
 #   scale = 1 
 # else:
 #   scale = 1000
  htp1000LH.Scale(scale) 
  htp1200LH.Scale(scale)
  #htp1500LH.Scale(1) 
  #htp1800LH.Scale(1) 
  hbkg = hqcd.Clone('kbkg')
  hbkg . Add(hsingletop) 
  hbkg . Add(httjets) 
  hbkg . Add(hwjets) 
  hbkg . Add(httw) 
  hbkg . Add(httz) 
#  hbkg . Add(hthq) 
#  hbkg . Add(hdy) 
  if doData:
    hratio = hdata.Clone('hratio')
    hratio.Divide(hbkg)
  
  fun = ROOT.TF1('fun','[0]*TMath::Exp([1]*x)+[2] ', 850, 400)
  #fun = ROOT.TF1('fun','[0] + [1]*x + [2]*x*x + [3]*x*x*x*x + [4]*x*x*x*x*x + [5]*x*x*x*x*x*x', 850, 4000)
  #fun = ROOT.TF1('fun','[0] + [1]*x + [2]*x*x', 1100, 3200)
  if doratiofit:
    fun.SetParameter(0,1.05)
    fun.SetParameter(1,-0.004)
    fun.SetParameter(2,0)
   # fun.SetParameter(3,0)
   # fun.SetParameter(4,0)
   # fun.SetParameter(5,0)
    fun.SetParName(0,'c')
    fun.SetParName(1,'b')
    fun.SetParName(2,'a')
   # fun.SetParName(3,'d')
   # fun.SetParName(4,'f')
   # fun.SetParName(5,'g')
    fitres = hratio.Fit('fun', 'S')
    cov = fitres.GetCovarianceMatrix()
    fitres.Print('V')
    #fitres.Write()
 # if doData:
  hdata       . SetMarkerStyle(20) 
  hdata       . SetLineStyle(1) 
  hdata       . SetLineWidth(2) 
  hdata       . SetLineColor(1)  
    
  hbkg        . SetLineStyle(1) 
  hbkg        . SetLineWidth(1) 
  hbkg        . SetLineColor(1)  
  hbkg        . SetFillColor(0)  
    
  hsingletop  . SetLineColor(46)  
  hwjets      . SetLineColor(36)  
  httjets     . SetLineColor(26)  
  hqcd        . SetLineColor(16)  
  httw        . SetLineColor(21)  
  httz        . SetLineColor(31)  
#  hthq        . SetLineColor(41)  
#  hdy         . SetLineColor(12)  
  
  htp1000LH     . SetLineColor(3)  
  htp1200LH     . SetLineColor(4)  
  #htp1500LH     . SetLineColor(5)  
  #htp1800LH     . SetLineColor(6)  
  
  htp1000LH     . SetLineWidth(2)  
  htp1200LH     . SetLineWidth(2)  
  #htp1500LH     . SetLineWidth(2)  
  #htp1800LH     . SetLineWidth(2)  
  
  htp1000LH     . SetLineStyle(1)  
  htp1200LH     . SetLineStyle(1)  
  #htp1500LH     . SetLineStyle(1)  
  #htp1800LH     . SetLineStyle(1)  
  
  hsingletop  . SetFillColor(46)  
  #hsingletop  . SetFillColor(46)  
  hwjets      . SetFillColor(36)  
  httjets     . SetFillColor(26)  
  hqcd        . SetFillColor(16)  
  httw        . SetFillColor(21)  
  httz        . SetFillColor(31)  
#  hthq        . SetFillColor(41)  
#  hdy         . SetFillColor(12)  
  
  htp1000LH     . SetFillColor(0)  
  htp1200LH     . SetFillColor(0)  
  #htp1500LH     . SetFillColor(0)  
  #htp1800LH     . SetFillColor(0)  
  if doData:
   hratio      . SetMarkerStyle(20) 
   hratio      . SetLineStyle(1) 
   hratio      . SetLineWidth(2) 
   hratio      . SetLineColor(1)  
    
  hsbkg = ROOT.THStack('hsbkg','')
  hsbkg.Add(httw)
  hsbkg.Add(httz)
#  hsbkg.Add(hthq)
#  hsbkg.Add(hdy)
  hsbkg.Add(hsingletop)
  hsbkg.Add(hwjets)
  hsbkg.Add(httjets)
  hsbkg.Add(hqcd)
 
  if doData: 
    c0 = ROOT.TCanvas('c_data_mc_'+hist,'',800,600)
  else:
    c0 = ROOT.TCanvas('c_mc_'+hist,'',800,600)
    
  ROOT.SetOwnership(c0,False)
  
  c0.cd()
  
  if doData:
    pad0 = ROOT.TPad("pad0","",0.0,0.3,1.0,1.0)
    pad1 = ROOT.TPad("pad1","",0.0,0.0,1.0,0.3)
  else:
    pad0 = ROOT.TPad("pad0","",0.0,0.1,1.0,1.0)
    
  if doLog:
    pad0.SetLogy()
  pad0.Draw() 
  pad0.cd()
  pad0.SetBottomMargin(0.05)
  if doData:
    hdata.GetYaxis().SetTitle(yLabel)
    hdata.GetXaxis().SetTitleSize(0.14*0.3/0.7)
    hdata.GetXaxis().SetTitleOffset(0.6) 
    hdata.GetYaxis().SetTitleSize(0.14*0.3/0.7)
    hdata.GetYaxis().SetLabelSize(0.14*0.3/0.7)
    hdata.GetYaxis().SetTitleOffset(0.35*7/3)
  else:
    hbkg.GetYaxis().SetTitle(yLabel)
    hbkg.GetXaxis().SetTitle(xLabel)
    hbkg.GetXaxis().SetTitleSize(0.14*0.3/0.7)
    hbkg.GetXaxis().SetTitleOffset(0.8) 
    hbkg.GetYaxis().SetTitleSize(0.14*0.3/0.7)
    hbkg.GetYaxis().SetLabelSize(0.14*0.3/0.7)
    hbkg.GetYaxis().SetTitleOffset(0.35*7/3)
    hbkg.GetYaxis().SetDecimals(False)
    ROOT.TGaxis.SetMaxDigits(3)
  if doData:
    hdata.Draw('e1')
    hsbkg.Draw('histsame')
  else:
    hbkg.Draw('hist')
    hsbkg.Draw('histsame')
  hbkg.Draw('histsame')
  if doData:
    hdata.Draw('e1same')
  htp1000LH.Draw('histsame')
  htp1200LH.Draw('histsame')
  #htp1500LH.Draw('histsame')
  #htp1800LH.Draw('histsame')

  if xlow < hdata.GetBinLowEdge(1):
    xlow = hdata.GetBinLowEdge(1)
  if xhigh > hdata.GetBinLowEdge(hdata.GetNbinsX()) + hdata.GetBinWidth(hdata.GetNbinsX()): 
    xhigh = hdata.GetBinLowEdge(hdata.GetNbinsX()) + hdata.GetBinWidth(hdata.GetNbinsX())

  if doData:
    hdata.GetXaxis().SetRangeUser(xlow,xhigh)
  
    hdata.GetXaxis().SetTitle(xLabel)
    hdata.GetXaxis().SetLabelSize(0)
  #else:
  #  hsbkg.GetXaxis().SetRangeUser(xlow,xhigh)
  #
  #  hsbkg.GetXaxis().SetTitle(xLabel)
  #  hsbkg.GetXaxis().SetLabelSize(0.14)
    
  pad0.RedrawAxis()
  
  pad0.Update()

  xmin = pad0.GetUxmin()
  if doData:
    ymin = hdata.GetMinimum()
  else:
    ymin = hbkg.GetMinimum()
  xmax = pad0.GetUxmax()
  if doData:
    ymax = max( [hdata.GetMaximum(), hbkg.GetMaximum(),httjets.GetMaximum(), hqcd.GetMaximum(), htp1200LH.GetMaximum()])	#
  else:
    ymax = max( [hbkg.GetMaximum(),httjets.GetMaximum(), hqcd.GetMaximum(), htp1200LH.GetMaximum()])	#
  print " pad0 Uymax = ", ymax
  if doLog:
    if doData: 
      hdata.SetMaximum(ymax*5000)
    else:
      hbkg.SetMaximum(ymax*5000)
  else:
    if doData:
      hdata.SetMaximum(ymax*2)
    else:
      hbkg.SetMaximum(ymax*2)
  if doData:
    hdata.SetMinimum(0.1)
  else:
    hbkg.SetMinimum(0.1)

  leg = ROOT.TLegend(0.12,0.66,0.88,0.88,'','brNDC')
  leg.SetBorderSize(0)
  leg.SetFillColor(0)
  leg.SetTextSize(0.03)
  leg.SetMargin(0.2)  
  leg.SetNColumns(4)
  leg.SetColumnSeparation(0.09)
  leg.SetEntrySeparation(0.1)
  if doData:
    leg.AddEntry(hdata      ,"Data            " , "ep")
  leg.AddEntry(hbkg       ,"Total background" , "fl")
  leg.AddEntry(hqcd       ,"Multijets       " , "fl")
  leg.AddEntry(httjets    ,"t#bar{t}+jets   " , "fl")
  leg.AddEntry(hwjets     ,"W+jets          " , "fl")
  leg.AddEntry(hsingletop ,"Single top: tW  " , "fl")
  leg.AddEntry(httz     ,"ttZ+jets        " , "fl")
  leg.AddEntry(httw     ,"ttW+jets        " , "fl")
#  leg.AddEntry(hdy     ,"DY+jets         " , "fl")
#  leg.AddEntry(hthq     ,"THQ             " , "fl")
  leg.AddEntry(htp1000LH    ,"#splitline{M(T) = 1800 GeV, 10%}{"+str(scale)+" pb xsec.}" , "fl")
  leg.AddEntry(htp1200LH    ,"#splitline{M(T) = 1200 GeV, 10%}{"+str(scale)+" pb xsec.}" , "fl")
  #leg.AddEntry(htp1500LH    ,"M(T) = 1200 GeV, Ttq RH, 1 pb " , "fl")
  #leg.AddEntry(htp1800LH    ,"M(T) = 1800 GeV, Ttq RH, 1 pb " , "fl")
  #leg.AddEntry(htp1800LH    ,"M(T) = 1800 GeV " , "fl")

  #if doratiofit:
  #  leg.AddEntry(fun        ,"Data/MC fit         " , "l" );

  leg.Draw()
  
  c0.cd()
  
  if doData:
    pad1.Draw() 
    pad1.cd()
    pad1.SetTopMargin(0.05)
    pad1.SetBottomMargin(0.4)
    hdata.GetXaxis().SetTitleSize(0)

    hratio.GetXaxis().SetTitle(hdata.GetXaxis().GetTitle())
    hratio.GetXaxis().SetTitleSize(0.14)
    hratio.GetXaxis().SetLabelSize(0.14)
    hratio.GetXaxis().SetTickLength(hdata.GetYaxis().GetTickLength())
    hratio.GetXaxis().SetTitleOffset(1.20)
    hratio.GetXaxis().SetNdivisions(510)

    hratio.GetYaxis().SetTitle("Data/MC")
    hratio.GetYaxis().SetTitleSize(0.14)
    hratio.GetYaxis().SetLabelSize(0.14)
    hratio.GetYaxis().SetTickLength(hdata.GetYaxis().GetTickLength())
    hratio.GetYaxis().SetTitleOffset(0.35)
    hratio.GetYaxis().SetNdivisions(504)
  
    hratio.Draw("e1")

    hratio.GetXaxis().SetRangeUser(xlow,xhigh)
    hratio.SetMinimum(0.5)
    hratio.SetMaximum(1.5)
    
  if doratiofit:
    fun.Draw('same')
    #fun2 = ROOT.TF1('fun2', '1.29308 - 2.71605e-4*x + 3.82408e-8*x*x', 1100, 3200)
    #fun2.SetLineColor(2)
    #fun2.Draw('SAME')
    pad1.Update()
    pavestats = hratio.FindObject("stats")
    pavestats.SetX1NDC(0.50)
    pavestats.SetX2NDC(0.88)
    pavestats.SetY1NDC(0.70)
    pavestats.SetY2NDC(0.92) 
    pavestats.SetBorderSize(0)
    pavestats.SetStatFormat('6.4f')
    pad1.Modified();  
  
  if doData:
    line = ROOT.TLine(xlow,1,xhigh,1)
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
  
  CMS_lumi.CMS_lumi(c0, 4, iPos, doLog, doData)
  c0.Update() 

  if doLog:
    isLog = 'log'
  else:
    isLog = 'linear'
  c0.SaveAs(outDir+'/'+c0.GetName()+'_'+isLog+region+'.pdf')    #  change date for new plots
  c0.SaveAs(outDir+'/'+c0.GetName()+'_'+isLog+region+'.png')  #  change date for new plots
