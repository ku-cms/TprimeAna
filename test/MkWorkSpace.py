#!/usr/bin/env python

from __future__ import print_function
import os, sys, re, imp, ROOT, copy
ROOT.gROOT.SetBatch()
ROOT.gSystem.Load('libHiggsAnalysisCombinedLimit.so')

debug = False

datacard2015_template='''datacard_template = """---------------------------------------------------------------------------------------
imax 1 number of channels
jmax 3 number of backgrounds
kmax * number of nuisance parameters (sources of systematical uncertainties)
---------------------------------------------------------------------------------------
shapes data_obs          RREG  ROOTFILENAME MTP_regionREG_data_obs
shapes PROCMASS          RREG  ROOTFILENAME MTP_regionREG_PROC_MASS_WIDTH_SP MTP_regionREG_PROC_MASS_WIDTH_SP_$SYSTEMATIC
shapes TTJets            RREG  ROOTFILENAME MTP_regionREG_TTJets MTP_regionREG_TTJets_$SYSTEMATIC
shapes Other             RREG  ROOTFILENAME MTP_regionREG_Other MTP_regionREG_Other_$SYSTEMATIC
shapes QCD               RREG  ROOTFILENAME MTP_regionREG_estQCD MTP_regionREG_estQCD_$SYSTEMATIC
---------------------------------------------------------------------------------------
bin                        RREG
observation                -1
---------------------------------------------------------------------------------
bin                        RREG               RREG          RREG         RREG
process                    PROCMASS           QCD           TTJets       Other
process                    0                  1             2            3
rate                       -1                 -1            -1           -1
-------------------------------------------------------------------------------
lumi               lnN     1.025              0.975/1.025   1.025/0.975  1.025/0.975 
purewt             lnN     1.03               0.97/1.03     1.03/0.97    1.03/0.97
pdfrewt            lnN     0.990/1.010        0.990/1.010   1.010/0.990  1.010/0.990
topxsec            lnN     -                  0.938/1.061   0.938/1.061  -
wxsec              lnN     -                  0.962/1.038   -            1.038/0.962
higgsShowerSf      lnN     1.1                0.90/1.10     1.10/0.90    1.10/0.90
t21Sf              lnN     1.125              0.875/1.125   1.125/0.875  1.125/0.875
higgstagmassJES    lnN     1.02               0.98/1.02     1.02/0.98    1.02/0.98
ShapeQCD           shape   -                 1.0            -             -            
ShapeTTJets        shape   -                 -              1.0           -            
ShapeOther         shape   -                 -              -             1.0          
bc                 shape   1.0               1.0            1.0           -            
l                  shape   1.0               1.0            1.0           -            
ttag               shape   1.0               1.0            1.0           -            
mufr               shape   1.0               1.0            1.0           -            
JES                shape   1.0               1.0            1.0           -            
JER                shape   1.0               1.0            1.0           -            
JMR                shape   1.0               1.0            1.0           -            
---------------------------------------------------------------------------------------
'''

datacard_template='''----------------------------------------------------------------------------------------------------------------------------------
imax 1 number of bins
jmax 3 number of processes minus 1
kmax * number of nuisance parameters
----------------------------------------------------------------------------------------------------------------------------------
shapes data_obs          RREG  WS w:MTP_regionREG_data_obs
shapes PROCMASS_WIDTH    RREG  WS w:MTP_regionREG_PROC_MASS_WIDTH_SP w:MTP_regionREG_PROC_MASS_WIDTH_SP_$SYSTEMATIC
shapes TTJets            RREG  WS w:MTP_regionREG_TTJets w:MTP_regionREG_TTJets_$SYSTEMATIC
shapes Other             RREG  WS w:MTP_regionREG_Other w:MTP_regionREG_Other_$SYSTEMATIC
shapes QCD               RREG  WS w:pdf_regionREG_QCD w:pdf_regionREG_QCD_$SYSTEMATIC
----------------------------------------------------------------------------------------------------------------------------------
bin                RREG      
observation        -1.0    
----------------------------------------------------------------------------------------------------------------------------------
bin                RREG                RREG              RREG            RREG           
process            PROCMASS_WIDTH      TTJets            Other           QCD          
process            0                   1                 2               3             
rate               -1                  -1                -1              1.00        
------------------------------------------------------------------------------------
lumi               lnN     1.025       1.025             1.025           -
purewt             lnN     1.03        1.03              1.03            -
topxsec            lnN     -           1.061             -               -
higgsShowerSf      lnN     1.10        1.10              1.10            -
t21Sf              lnN     1.125       1.125             1.125           -
higgstagmassJES    lnN     1.02        1.02              1.02            -
ShapeTTJets        shape   -           1.0               -               -            
ShapeOther         shape   -           -                 1.0             -            
ShapeQCD           shape   -           -                 -               1.0          
bc                 shape   1.0         1.0               1.0             -            
l                  shape   1.0         1.0               1.0             -            
ttag               shape   1.0         1.0               1.0             -            
mufr               shape   1.0         1.0               1.0             -            
JES                shape   1.0         1.0               1.0             -            
JER                shape   1.0         1.0               1.0             -            
JMR                shape   1.0         1.0               1.0             -            
'''

datacard_regionsAC_rate='''ABCDrate     lnU     -                   -                 -               0.4/1.6      
----------------------------------------------------------------------------------------------------------------------------------
QCD_CH_RREG_norm rateParam RREG QCD 1
----------------------------------------------------------------------------------------------------------------------------------
'''

datacard_regionsB_rate='''ABCDrate     lnU     -                   -                 -               1.6/0.4      
----------------------------------------------------------------------------------------------------------------------------------
QCD_CH_RREG_norm rateParam RREG QCD 1
----------------------------------------------------------------------------------------------------------------------------------
'''

datacard_regionD_rate='''ABCDrate     lnU     -                   -                 -               1.6/0.4
----------------------------------------------------------------------------------------------------------------------------------
QCD_CH_RD_norm    rateParam RD QCD       (@0*@1)/@2 QCD_CH_RB_norm,QCD_CH_RC_norm,QCD_CH_RA_norm
----------------------------------------------------------------------------------------------------------------------------------
'''

datacard_toy_regionD_rate='''ABCDrate     lnU     -                   -                 -               1.6/0.4
----------------------------------------------------------------------------------------------------------------------------------
QCD_CH_RD_norm    rateParam RD QCD 1
----------------------------------------------------------------------------------------------------------------------------------
'''

def MkDatacard(carddir, proc, mass, width, spin, channel, reg, ws):
  if not os.path.exists(os.path.join(os.getcwd(),carddir)):
    os.mkdir(carddir)
  card = open(os.path.join(carddir, 'datacard_{0}_{1}_{2}_R{3}.txt'.format(proc, mass+'_'+width, channel, reg)), 'w')
  card_contents = re.sub('PROC', proc,    datacard_template)
  card_contents = re.sub('MASS', mass,    card_contents)
  card_contents = re.sub('WIDTH',width,   card_contents)
  card_contents = re.sub('SP'   ,spin,    card_contents)
  card_contents = re.sub('REG',  reg,     card_contents)
  card_contents = re.sub('WS',   ws,      card_contents)

  if 'D' in reg:
    rate_lines = datacard_regionD_rate
  elif 'B' in reg:
    rate_lines = re.sub('REG', reg, datacard_regionsB_rate)
  elif map(lambda r: r in reg, ['A', 'B', 'C']):
    rate_lines = re.sub('REG', reg, datacard_regionsAC_rate)
  rate_lines = re.sub('CH', channel, rate_lines)
  card_contents += rate_lines

  card.write(card_contents)
  card.close()

  if 'D' in reg:
    if width == '00p':
      print("Doing 2015-style datacards")
      card = open(os.path.join(carddir, 'datacard2015_{0}_{1}_{2}_R{3}.txt'.format(proc, mass, channel, reg)), 'w')
      card_contents = re.sub('PROC', proc,    datacard2015_template)
      card_contents = re.sub('MASS', mass,    card_contents)
      card_contents = re.sub('WIDTH',width,   card_contents)
      card_contents = re.sub('SP'   ,spin,    card_contents)
      card_contents = re.sub('REG',  reg,     card_contents)
      card_contents = re.sub('ROOTFILENAME',  ws.replace('workspace', 'template'), card_contents)
      card.write(card_contents)
      card.close()

    card = open(os.path.join(carddir, 'datacard_{0}_{1}_{2}_R{3}_toy.txt'.format(proc, mass+'_'+width, channel, reg)), 'w')
    card_contents = re.sub('PROC', proc,    datacard_template)
    card_contents = re.sub('MASS', mass,    card_contents)
    card_contents = re.sub('WIDTH',width,   card_contents)
    card_contents = re.sub('SP'   ,spin,    card_contents)
    card_contents = re.sub('REG',  reg,     card_contents)
    card_contents = re.sub('WS',   ws,      card_contents)
    rate_lines = datacard_toy_regionD_rate
    rate_lines = re.sub('CH', channel, rate_lines)
    card_contents += rate_lines
    card.write(card_contents)
    card.close()

def GetProcs():

  chs = [
      'TbtH'  , 
      'TbtZ'  ,  
      'TttH'  , 
      'TttZ'  , 
      'TbtHtZ', 
      'TttHtZ', 
      ]

  widths = ['00p', '10p', '20p', '30p']

  d={}
  for w in widths:
    d[w] = []
  sigs={}
  for ch in chs:
    sigs[ch] = copy.deepcopy(d)

  sigs['TbtH']['00p']        = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1700, 1800, 2000, 2200, 2400, 2600]
  sigs['TbtZ']['00p']        = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1700, 1800]
  sigs['TttH']['00p']        = sigs['TbtH']['00p']
  sigs['TttZ']['00p']        = sigs['TbtZ']['00p']
  sigs['TbtHtZ']['00p']      = sigs['TbtZ']['00p']
  sigs['TttHtZ']['00p']      = sigs['TbtZ']['00p']

  sigs['TbtH']['10p']     = [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
  sigs['TbtZ']['10p']     = [800, 1000, 1200, 1400, 1600, 1800, 2000]
  sigs['TttH']['10p']     = sigs['TbtH']['10p']
  sigs['TttZ']['10p']     = sigs['TbtZ']['10p']
  sigs['TbtHtZ']['10p']   = sigs['TbtZ']['10p']
  sigs['TttHtZ']['10p']   = sigs['TbtZ']['10p']

  sigs['TbtH']['20p']     = [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
  sigs['TbtZ']['20p']     = [800, 1200, 1400, 1600, 1800, 2000]
  sigs['TttH']['20p']     = [800, 1000, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
  sigs['TttZ']['20p']     = [800, 1200, 1400, 1600, 1800, 2000]
  sigs['TbtHtZ']['20p']   = sigs['TbtZ']['20p']
  sigs['TttHtZ']['20p']   = [800, 1400, 1600, 1800, 2000]

  sigs['TbtH']['30p']     = [800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600]
  sigs['TbtZ']['30p']     = [800, 1000, 1200, 1400, 1600, 1800, 2000]
  sigs['TttH']['30p']     = [800, 1000, 1200, 1400, 1600, 1800, 2200, 2400, 2600]
  sigs['TttZ']['30p']     = [800, 1000, 1200, 1400, 1600, 1800, 2000]
  sigs['TbtHtZ']['30p']   = sigs['TbtZ']['30p']
  sigs['TttHtZ']['30p']   = [800, 1000, 1200, 1400, 1600, 1800]

  print(sigs)

  procs={
      'data_obs'            : {'A': [], 'C': [], 'B': [], 'D': []}, 
      'QCD'                 : {'A': [], 'C': [], 'B': [], 'D': []}, 
      'TTJets'              : {'A': [], 'C': [], 'B': [], 'D': []}, 
      'Other'               : {'A': [], 'C': [], 'B': [], 'D': []}, 
      } 

  for sig in sigs:
    if sig[:2] == 'Tb': spin = 'LH'
    elif sig[:2] == 'Tt': spin = 'RH'
    for w in sigs[sig]:
      masses = sigs[sig][w]
      if len(masses) == 0: continue
      else:
        for m in masses:
          procname = '{0}_{1}_{2}_{3}'.format(sig, m, w, spin)
          procs[procname] = {'A': [], 'C': [], 'B': [], 'D': []}

  return procs, sigs


def MkWorkSpaceAndCards(fname, carddir):

  procs, sigs= GetProcs()

  print(procs)

  systs=[
      'JER', 
      'JMR', 
      'JES', 
      'Shape', 
      'Stat', 
      'bc', 
      'l', 
      'mufr', 
      'ttag', 
      ]

  w = ROOT.RooWorkspace('w')

  lo=600
  hi=3100
  nbins=50
  v_mass = ROOT.RooRealVar('m', 'm (T) [GeV]', lo, hi)
  l_mass = ROOT.RooArgList(v_mass)
  s_mass = ROOT.RooArgSet(v_mass)

  fin = ROOT.TFile.Open(fname, 'READ')

  for p, regs in procs.items():
    for r in regs:

      if p == 'QCD' and r == 'D': p = 'estQCD'

      print('>>>>>>>> MkWorkSpaceAndCards: Getting nominal histo for "MTP_region{0}_{1}"'.format(r, p))

      h = fin.Get("MTP_region{0}_{1}".format(r, p))
      #h.Rebin(2)

      nbins = h.GetNbinsX()
      if debug: print(">>>>>>>> MkWorkSpaceAndCards: h {0} has {1} bins".format(h.GetName(), nbins))
      lo = h.GetBinLowEdge(1)
      hi = h.GetBinLowEdge(nbins+1)
      v_mass.setBins(nbins)
  
      if 'QCD' in p: h.Scale(1./h.Integral())

      print('>>>>>>>> MkWorkSpaceAndCards: hname  {0}'.format(h.GetName()))

      #REMif 'Tb' in p or 'Tt' in p:
      #REM  if len(p.split('_')) < 4: p = '{0}_{1}_{2}_{3}'.format(p.split('_')[0], p.split('_')[1], '00p', p.split('_')[2])

      roohist = ROOT.RooDataHist("MTP_region{0}_{1}".format(r, p.replace('estQCD', 'QCD')), "MTP_region{0}_{1}".format(r, p.replace('estQCD', 'QCD')), l_mass, h)

      if debug: print(">>>>>>>> MkWorkSpaceAndCards: roohist {0} has {1} bins".format(roohist.GetName(), roohist.numEntries()))

      getattr(w, 'import')(roohist)

      if 'QCD' in p:
        roohistpdf = ROOT.RooHistPdf("pdf_region{0}_{1}".format(r, p.replace('estQCD', 'QCD')), "pdf_region{0}_{1}".format(r, p.replace('estQCD', 'QCD')), s_mass, roohist)
        getattr(w, 'import')(roohistpdf)

        bkg_norm = ROOT.RooRealVar("pdf_region{0}_{1}_norm".format(r, p.replace('estQCD', 'QCD')), "pdf_region{0}_{1}_norm".format(r, p.replace('estQCD', 'QCD')), h.Integral())
        getattr(w, 'import')(bkg_norm, ROOT.RooFit.RecycleConflictNodes())

      if 'Data' in p: continue

      for s in systs:
        print('>>>>>>>> MkWorkSpaceAndCards: Getting syst histo for proc {0} reg {1} syst {2}'.format(p, r, s))

        if 'Shape' in s: s = 'Shape{0}'.format(p.replace('estQCD', 'QCD'))
        if r != 'D': s = s.replace('QCD', '')

        hsystup = fin.Get("MTP_region{0}_{1}_{2}Up".format(r, p, s))
        hsystdown = fin.Get("MTP_region{0}_{1}_{2}Down".format(r, p, s))

        if not hsystup or not hsystdown: continue

        #hsystup.Rebin(2)
        #hsystdown.Rebin(2)

        if 'QCD' in p and 'Shape' in s and 'QCD' not in s: s = s+'QCD'
         
        roohistup = ROOT.RooDataHist("MTP_region{0}_{1}_{2}Up".format(r, p.replace('estQCD', 'QCD'), s), "MTP_region{0}_{1}_{2}Up".format(r, p.replace('estQCD', 'QCD'), s), l_mass, hsystup)
        roohistdown = ROOT.RooDataHist("MTP_region{0}_{1}_{2}Down".format(r, p.replace('estQCD', 'QCD'), s), "MTP_region{0}_{1}_{2}Down".format(r, p.replace('estQCD', 'QCD'), s), l_mass, hsystdown)

        getattr(w, 'import')(roohistup)
        getattr(w, 'import')(roohistdown)

        if 'QCD' in p:
         
          roohistpdfUp   = ROOT.RooHistPdf("pdf_region{0}_{1}_{2}Up".format(r, p.replace('estQCD', 'QCD'), s), "pdf_region{0}_{1}_{2}Up".format(r, p.replace('estQCD', 'QCD'), s), s_mass, roohistup)
          roohistpdfDown = ROOT.RooHistPdf("pdf_region{0}_{1}_{2}Down".format(r, p.replace('estQCD', 'QCD'), s), "pdf_region{0}_{1}_{2}Down".format(r, p.replace('estQCD', 'QCD'), s), s_mass, roohistdown)

          getattr(w, 'import')(roohistpdfUp)
          getattr(w, 'import')(roohistpdfDown)

      ###Making datacard
      if re.match('Tb', p) != None or re.match('Tt', p) != None:
        print(p.split('_'))
        ch = fname.split('_')[1]
        mass = p.split('_')[1]
        width = p.split('_')[2]
        #REMif len(p.split('_')) > 3: 
        #REM  width = p.split('_')[2]
        #REMelse: 
        #REM  width = '00p'
        print('Making datacard proc {0} mass {1} channel {2} region {3}'.format(p.split('_')[0], mass, ch, r))
        if 'Tb' in p: spin = 'LH'
        elif 'Tt' in p: spin = 'RH'
        MkDatacard(carddir,p.split('_')[0], mass, width, spin, ch, r, fname.replace('template', 'workspace'))

  if not os.path.exists('workspaces'): os.mkdir('workspaces')
  w.writeToFile(fname.replace('template', 'workspace'))

  print("Workspace made and written to file!")

def CombineCards(carddir):
  print("Combining cards")

  procs, sigs = GetProcs()
  chs = ['tH', 'tZ']
  regs = ['A', 'B', 'C', 'D']

  pwd = os.getcwd()
  for p in sigs: 
    widths = sigs[p]
    for w in widths:
      masses = sigs[p][w]
      for m in masses: 
        cards = ' '
        cards_toy = ' '
        for ch in chs:
          for r in regs:
            #REMif not w: w = '00p'
            cards = cards + '{2}_R{3}=datacard_{0}_{1}_{2}_R{3}.txt '.format(p, str(m)+'_'+w, ch, r)
            if r == 'D':
              cards_toy = cards_toy + '{2}_R{3}=datacard_{0}_{1}_{2}_R{3}_toy.txt '.format(p, str(m)+'_'+w, ch, r)
            else:
              cards_toy = cards_toy + '{2}_R{3}=datacard_{0}_{1}_{2}_R{3}.txt '.format(p, str(m)+'_'+w, ch, r)

        cmd_template = 'combineCards.py CARDS > datacard_PROC_MASS_WIDTH.txt'
        cmd_template = re.sub('CARDS', cards, cmd_template)
        cmd_template = re.sub('PROC', p, cmd_template)
        cmd_template = re.sub('MASS', str(m), cmd_template)
        cmd_template = re.sub('WIDTH', w, cmd_template)
        cmd_template = re.sub('DATACARDPATH', carddir, cmd_template)
        print(cmd_template)

        os.chdir(os.path.join(pwd,carddir))
        os.system(cmd_template)
        os.chdir(pwd) 
        os.system('text2workspace.py {0}/datacard_{1}_{2}_{3}.txt'.format(carddir, p, m, w))

        cmd_template_toy = 'combineCards.py CARDS > datacard_PROC_MASS_WIDTH_toy.txt'
        cmd_template_toy = re.sub('CARDS', cards_toy, cmd_template_toy)
        cmd_template_toy = re.sub('PROC', p, cmd_template_toy)
        cmd_template_toy = re.sub('MASS', str(m), cmd_template_toy)
        cmd_template_toy = re.sub('WIDTH', w, cmd_template_toy)
        cmd_template_toy = re.sub('DATACARDPATH', carddir, cmd_template_toy)
        print(">>>Eexecuting "+cmd_template_toy)

        os.chdir(os.path.join(pwd,carddir))
        os.system(cmd_template_toy)
        os.chdir(pwd) 
        os.system('text2workspace.py {0}/datacard_{1}_{2}_{3}_toy.txt'.format(carddir, p, m, w))
        submitAsymptotic(p, m, w, carddir)

import re, subprocess

asym_template='''#!/bin/bash


workdir=WORKDIR
rundir=RUNDIR

cd ${workdir}
eval `scramv1 runtime -sh`
cd ${rundir}

combine -M FitDiagnostics -s 123456 -m MASS -d ../CARDDIR/datacard_PROC_MASS_WIDTH_toy.root --expectSignal 0 -t 1 --saveToys --setParameters QCD_tH_RA_norm=424,QCD_tH_RB_norm=58,QCD_tH_RC_norm=112,QCD_tH_RD_norm=15,QCD_tZ_RA_norm=5584.79,QCD_tZ_RB_norm=607.636,QCD_tZ_RC_norm=243.204,QCD_tZ_RD_norm=26.4611 --cminDefaultMinimizerTolerance=0.2  --cminFallbackAlgo Minuit,0.001 --rMin -1.0 --rMax 1.0
combine -M AsymptoticLimits -s 123456 -m MASS -d ../CARDDIR/datacard_PROC_MASS_WIDTH.root -t 1 --toysFile higgsCombineTest.FitDiagnostics.mHMASS.123456.root --run expected --expectSignal 0 -v 5 --rMin -0.1 --rMax 5 --cminPoiOnlyFit --cminPreScan --cminDefaultMinimizerTolerance=0.2 >& AsymptoticLimits_PROC_MASS.log
mv higgsCombineTest.AsymptoticLimits.mHMASS.123456.root higgsCombineTest.AsymptoticLimits.mHMASS_WIDTH.123456.root


cd ${workdir}

'''

def submitAsymptotic(sig, m, w, carddir):

  workdir = os.getcwd()

  rundir=os.path.join(workdir, 'limSig_{0}_{1}_{2}_Toy'.format(sig, m, w))
  if not os.path.exists(rundir): os.mkdir(rundir)

  run_script = re.sub('WORKDIR', workdir, asym_template)
  run_script = re.sub('RUNDIR', rundir, run_script)
  run_script = re.sub('PROC', sig, run_script)
  run_script = re.sub('MASS', str(m), run_script)
  run_script = re.sub('WIDTH', w, run_script)
  run_script = re.sub('CARDDIR', carddir, run_script)
  card = open(os.path.join(rundir, 'bash_{0}_{1}_{2}.sh'.format(sig, m, w)), 'w')
  card.write(run_script)
  card.close()

  os.chdir(rundir)
  print('>>>>Running {}'.format(os.path.join(rundir, 'bash_{0}_{1}_{2}.sh'.format(sig, m, w))))
  subprocess.check_output(['/bin/bash', os.path.join(rundir, 'bash_{0}_{1}_{2}.sh'.format(sig, m, w))])

  os.chdir(workdir)

def runAsymptotic(carddir):

  workdir = os.getcwd()

  procs, sigs = GetProcs()

  print(sigs)

  for sig in sigs:
    widths_masses = sigs[sig]
    for w in widths_masses:
      for m in widths_masses[w]:

        #REMif not w: w = '00p'

        rundir=os.path.join(workdir, 'limSig_{0}_{1}_{2}_Toy'.format(sig, m, w))
        if not os.path.exists(rundir): os.mkdir(rundir)

        run_script = re.sub('WORKDIR', workdir, asym_template)
        run_script = re.sub('PROC', sig, run_script)
        run_script = re.sub('MASS', str(m), run_script)
        run_script = re.sub('WIDTH', w, run_script)
        run_script = re.sub('CARDDIR', carddir, run_script)
        card = open(os.path.join(rundir, 'bash_{0}_{1}_{2}.sh'.format(sig, m, w)), 'w')
        card.write(run_script)
        card.close()

        os.chdir(rundir)
        print('>>>>Running {}'.format(os.path.join(rundir, 'bash_{0}_{1}_{2}.sh'.format(sig, m, w))))
        subprocess.check_output(['/bin/bash', os.path.join(rundir, 'bash_{0}_{1}_{2}.sh'.format(sig, m, w))])

        os.chdir(workdir)

def main():

  usage='''
  Takes 3 arguments: (i) the tH selection templates, (ii) the tZ selection templates, (iii) the dir to write the datacards.
  python MkWorkSpace.py templates/template_tH_forwardJetVeto_looseBTop_1Mar18_smoothed.root templates/template_tZ_forwardJetVeto_looseBTop_1Mar18_smoothed.root datacards_fwdjetveto_looseb/
  '''

  if len(sys.argv) < 3: 
    sys.exit(usage)

  import functools
  map(functools.partial(MkWorkSpaceAndCards, carddir=sys.argv[-1]), sys.argv[1:-1])
  CombineCards(sys.argv[-1])
  #runAsymptotic(sys.argv[-1])

if __name__ == "__main__":
  main()
