#!/usr/bin/env python

import ROOT as rt
import array

def subjetEff(inFile, jetType, fileOut):
    disc = 0.5426

    f = rt.TFile(inFile, 'r')
    t = f.Get('ana'+jetType+'/tree')

    nAK8 = array.array('i', [0])
    ptAK8 = rt.vector('double')()
    etaAK8 = rt.vector('double')()
    sj0CSV = rt.vector('double')()
    sj1CSV = rt.vector('double')()
    sj0Flavour = rt.vector('double')()
    sj1Flavour = rt.vector('double')()

    t.SetBranchAddress('SelectedEvent_nAK8', nAK8)
    t.SetBranchAddress('ptAK8', ptAK8)
    t.SetBranchAddress('etaAK8', etaAK8)
    t.SetBranchAddress('sj0CSVAK8', sj0CSV)
    t.SetBranchAddress('sj1CSVAK8', sj1CSV)
    t.SetBranchAddress('hadronFlavourSJ0AK8', sj0Flavour)
    t.SetBranchAddress('hadronFlavourSJ1AK8', sj1Flavour) 

    h_num_b = rt.TH2D("num_b", "Numerator for b in "+inFile.split('/')[-1].split('.')[0],50,200,1000,24,0,2.4)
    h_num_c = rt.TH2D("num_c", "Numerator for c in "+inFile.split('/')[-1].split('.')[0],50,200,1000,24,0,2.4)
    h_num_l = rt.TH2D("num_l", "Numerator for l in "+inFile.split('/')[-1].split('.')[0],50,200,1000,24,0,2.4)
    h_denom_b = rt.TH2D("denom_b", "Denominator for b in "+inFile.split('/')[-1].split('.')[0],50,200,1000,24,0,2.4)
    h_denom_c = rt.TH2D("denom_c", "Denominator for c in "+inFile.split('/')[-1].split('.')[0],50,200,1000,24,0,2.4)
    h_denom_l = rt.TH2D("denom_l", "Denominator for l in "+inFile.split('/')[-1].split('.')[0],50,200,1000,24,0,2.4)
    h_eff_b = rt.TH2D("eff_b", "Efficiency for b in "+inFile.split('/')[-1].split('.')[0],50,200,1000,24,0,2.4)
    h_eff_c = rt.TH2D("eff_c", "Efficiency for c in "+inFile.split('/')[-1].split('.')[0],50,200,1000,24,0,2.4)
    h_eff_l = rt.TH2D("eff_l", "Efficiency for l in "+inFile.split('/')[-1].split('.')[0],50,200,1000,24,0,2.4)



    for iEvent in xrange(0,t.GetEntries()):
        if iEvent %1000 is 0:
            print iEvent

        t.GetEntry(iEvent)
        for ijet in range(int(nAK8[0])):
            if int(sj0Flavour[ijet]) == 5:
                h_denom_b.Fill(ptAK8[ijet], abs(etaAK8[ijet]))
                if sj0CSV[ijet] > disc:
                    h_num_b.Fill(ptAK8[ijet], abs(etaAK8[ijet]))
            elif int(sj0Flavour[ijet]) == 4:
                h_denom_c.Fill(ptAK8[ijet], abs(etaAK8[ijet]))
                if sj0CSV[ijet] > disc:
                    h_num_c.Fill(ptAK8[ijet], abs(etaAK8[ijet]))
            else:
                h_denom_l.Fill(ptAK8[ijet], abs(etaAK8[ijet]))
                if sj0CSV[ijet] > disc:
                    h_num_l.Fill(ptAK8[ijet], abs(etaAK8[ijet]))

            if int(sj1Flavour[ijet]) == 5:
                h_denom_b.Fill(ptAK8[ijet], abs(etaAK8[ijet]))
                if sj1CSV[ijet] > disc:
                    h_num_b.Fill(ptAK8[ijet], abs(etaAK8[ijet]))
            elif int(sj1Flavour[ijet]) == 4:
                h_denom_c.Fill(ptAK8[ijet], abs(etaAK8[ijet]))
                if sj1CSV[ijet] > disc:
                    h_num_c.Fill(ptAK8[ijet], abs(etaAK8[ijet]))
            else:
                h_denom_l.Fill(ptAK8[ijet], abs(etaAK8[ijet]))
                if sj1CSV[ijet] > disc:
                    h_num_l.Fill(ptAK8[ijet], abs(etaAK8[ijet]))

    h_eff_b.Divide(h_num_b,h_denom_b)
    h_eff_c.Divide(h_num_c,h_denom_c)
    h_eff_l.Divide(h_num_l,h_denom_l)

    fout = rt.TFile(fileOut, 'recreate')
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
    subjetEff('./TbtH_1200_LH.root', 'CHS', './TbtH_1200_LH_btagEff_loose.root')
