#!/usr/bin/env python

import ROOT as rt
import sys
import array
from input_anaTp_cfi import *

def subjetEff(inFile, jetType, fileOut):
    disc

    f = rt.TFile(inFile, 'r')
    t = f.Get('ana'+jetType+'/tree')

    nAK8 = array.array('d', [0])
    ptAK8 = array.array('d', [0])
    etaAK8 = array.array('d', [0])
    sj0CSV = array.array('d', [0])
    sj1CSV = array.array('d', [0])
    sj0Flavour = array.array('i', [0])
    sj1Flavour = array.array('i', [0])

    t.SetBranchAddress('SelectedEvent_nAK8', nAK8)
    t.SetBranchAddress('ptAK8', ptAK8)
    t.SetBranchAddress('etaAK8', etaAK8)
    t.SetBranchAddress('sj0CSVAK8', sj0CSV)
    t.SetBranchAddress('sj1CSVAK8', sj1CSV)
    t.SetBranchAddress('hadronFlavourSJ0AK8', sj0Flavour)
    t.SetBranchAddress('hadronFlavourSJ1AK8', sj1Flavour) 

    h_num_b = rt.TH2D("num_b", "Numerator for b in "+inFile.split('/')[-1].split('.')[0])
    h_num_c = rt.TH2D("num_c", "Numerator for c in "+inFile.split('/')[-1].split('.')[0])
    h_num_l = rt.TH2D("num_l", "Numerator for l in "+inFile.split('/')[-1].split('.')[0])
    h_denom_b = rt.TH2D("denom_b", "Denominator for b in "+inFile.split('/')[-1].split('.')[0])
    h_denom_c = rt.TH2D("denom_c", "Denominator for c in "+inFile.split('/')[-1].split('.')[0])
    h_denom_l = rt.TH2D("denom_l", "Denominator for l in "+inFile.split('/')[-1].split('.')[0])
    h_eff_b = rt.TH2D("eff_b", "Efficiency for b in "+inFile.split('/')[-1].split('.')[0])
    h_eff_c = rt.TH2D("eff_c", "Efficiency for c in "+inFile.split('/')[-1].split('.')[0])
    h_eff_l = rt.TH2D("eff_l", "Efficiency for l in "+inFile.split('/')[-1].split('.')[0])



    for iEvent in xrange(t.GetEntries()):
        if iEvent %1000 is 0:
            print iEvent

        t.GetEntry(iEvent)

        for ijet in range(nAK8[0]):
            
            if sj0Flavour[0][ijet] is 5:
                h_denom_b.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet])
                if sj0CSV[0][ijet] > disc:
                    h_num_b.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet]))
            elif sj0Flavour[0][ijet] is 4:
                h_denom_c.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet])
                if sj0CSV[0][ijet] > disc:
                    h_num_c.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet]))
            else:
                h_denom_l.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet])
                if sj0CSV[0][ijet] > disc:
                    h_num_l.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet]))

            if sj1Flavour[0][ijet] is 5:
                h_denom_b.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet])
                if sj1CSV[0][ijet] > disc:
                    h_num_b.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet]))
            elif sj1Flavour[0][ijet] is 4:
                h_denom_c.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet])
                if sj1CSV[0][ijet] > disc:
                    h_num_c.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet]))
            else:
                h_denom_l.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet])
                if sj1CSV[0][ijet] > disc:
                    h_num_l.Fill(ptAK8[0][ijet], abs(etaAK8[0][ijet]))

    h_eff_b.Divide(h_num_b,h_denom_b)
    h_eff_c.Divide(h_num_c,h_denom_c)
    h_eff_l.Divide(h_num_l,h_denom_l)

    fout = rt.TFile(fileOut, 'w')
    h_num_b.Write()
    h_num_c.Write()
    h_num_l.Write()
    h_denom_b.Write()
    h_denom_c.Write()
    h_denom_l.Write()
    h_eff_b.Write()
    h_eff_c.Write()
    h_eff_l.Write()
    fout.Close()

if __name__ == "__main__":
    subjetEff('TbtH_1200_LH.root', 'CHS', 'btagEff.root')
