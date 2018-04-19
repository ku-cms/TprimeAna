#!/usr/bin/env python

import sys

import ROOT as rt
import numpy as np
import array
import math

CSVv2L = 0.5426
CSVv2M = 0.8484
CSVv2T = 0.9535
tag0p1 = 0.5
tag0p3 = 0.57

def reduceTree(treeList, inputFile, outputFile):

    oldFile = rt.TFile(inputFile, 'READ')
    hNoWt = oldFile.Get('allEvents/hEventCount_nowt')
    hWt = oldFile.Get('allEvents/hEventCount_wt')
    newFile = rt.TFile(outputFile, 'RECREATE')
    allEvtDir = rt.gDirectory.mkdir('allEvents')
    allEvtDir.cd()
    hNoWt.Write()
    hWt.Write()
    for tree in treeList:
        oldTree = oldFile.Get('ana'+tree+'/tree')
        rt.SetOwnership(oldTree,True)
        newFile.cd()
        newDir = rt.gDirectory.mkdir('ana'+tree)
        newDir.cd()
        newTree = oldTree.CloneTree(0)
        rt.SetOwnership(newTree,True)
   
        pMassOld = rt.vector('double')()
        pMassNew = rt.vector('double')()

        ptTopTaggedM = rt.vector('double')()
        etaTopTaggedM = rt.vector('double')()
        phiTopTaggedM = rt.vector('double')()
        MTopTaggedM = rt.vector('double')()
        sj0csvTopTaggedM = rt.vector('double')()
        sj1csvTopTaggedM = rt.vector('double')()
        tau32TopTaggedM = rt.vector('double')()

        ptTopTagged0M = rt.vector('double')()
        etaTopTagged0M = rt.vector('double')()
        phiTopTagged0M = rt.vector('double')()
        MTopTagged0M = rt.vector('double')()
        sj0csvTopTagged0M = rt.vector('double')()
        sj1csvTopTagged0M = rt.vector('double')()
        tau32TopTagged0M = rt.vector('double')()

        ptHTagged1M1L = rt.vector('double')()
        etaHTagged1M1L = rt.vector('double')()
        phiHTagged1M1L = rt.vector('double')()
        MHTagged1M1L = rt.vector('double')()
        prunedMassHTagged1M1L = rt.vector('double')()
        sj0csvHTagged1M1L = rt.vector('double')()
        sj1csvHTagged1M1L = rt.vector('double')()
        tau21HTagged1M1L = rt.vector('double')()

        ptHTagged1M0L = rt.vector('double')()
        etaHTagged1M0L = rt.vector('double')()
        phiHTagged1M0L = rt.vector('double')()
        MHTagged1M0L = rt.vector('double')()
        sj0csvHTagged1M0L = rt.vector('double')()
        sj1csvHTagged1M0L = rt.vector('double')()
        tau21HTagged1M0L = rt.vector('double')()

        ptZTagged1M1L = rt.vector('double')()
        etaZTagged1M1L = rt.vector('double')()
        phiZTagged1M1L = rt.vector('double')()
        MZTagged1M1L = rt.vector('double')()
        sj0csvZTagged1M1L = rt.vector('double')()
        sj1csvZTagged1M1L = rt.vector('double')()
        tau21ZTagged1M1L = rt.vector('double')()

        ptZTagged0L = rt.vector('double')()
        etaZTagged0L = rt.vector('double')()
        phiZTagged0L = rt.vector('double')()
        MZTagged0L = rt.vector('double')()
        sj0csvZTagged0L = rt.vector('double')()
        sj1csvZTagged0L = rt.vector('double')()
        tau21ZTagged0L = rt.vector('double')()

        btZ = np.zeros(1, dtype=np.float64)
        btZbU = np.zeros(1, dtype=np.float64)
        btZbD = np.zeros(1, dtype=np.float64)
        btZlU = np.zeros(1, dtype=np.float64)
        btZlD = np.zeros(1, dtype=np.float64)
        bt = np.zeros(1, dtype=np.float64)
        btbU = np.zeros(1, dtype=np.float64)
        btbD = np.zeros(1, dtype=np.float64)
        btlU = np.zeros(1, dtype=np.float64)
        btlD = np.zeros(1, dtype=np.float64)

        mtprimeATilde = np.zeros(1, dtype=np.float64)
        mtprimeBTilde = np.zeros(1, dtype=np.float64)
        mtprimeCTilde = np.zeros(1, dtype=np.float64)
        mtprimeDTilde = np.zeros(1, dtype=np.float64)

        isRegionA_tM = np.zeros(1, dtype=int)
        isRegionB_tM = np.zeros(1, dtype=int)
        isRegionC_tM = np.zeros(1, dtype=int)
        isRegionD_tM = np.zeros(1, dtype=int)

        isTopLeadingJet = np.zeros(1, dtype=int)
        isHiggsLeadingJet = np.zeros(1, dtype=int)
        isZLeadingJet = np.zeros(1, dtype=int)
        higgsAnul = rt.vector('int')() 
        higgsAnul += [0,0,0,0,0,0,0,0,0]
        ZAnul = rt.vector('int')() 
        ZAnul += [0,0,0,0,0,0,0,0,0]
        mtprimeATilde_tM = np.zeros(1, dtype=np.float64)
        mtprimeBTilde_tM = np.zeros(1, dtype=np.float64)
        mtprimeCTilde_tM = np.zeros(1, dtype=np.float64)
        mtprimeDTilde_tM = np.zeros(1, dtype=np.float64)

        mtprimeA_tM = np.zeros(1, dtype=np.float64)
        mtprimeB_tM = np.zeros(1, dtype=np.float64)
        mtprimeC_tM = np.zeros(1, dtype=np.float64)
        mtprimeD_tM = np.zeros(1, dtype=np.float64)

        isRegionD_tM_H1M0L = np.zeros(1, dtype=int)
        mtprimeDTilde_tM_H1M0L = np.zeros(1, dtype=np.float64)
        mtprimeD_tM_H1M0L = np.zeros(1, dtype=np.float64)

        isRegionA_tM_H1M0L = np.zeros(1, dtype=int)
        isRegionB_tM_H1M0L = np.zeros(1, dtype=int)
        isRegionC_tM_H1M0L = np.zeros(1, dtype=int)
        mtprimeATilde_tM_H1M0L = np.zeros(1, dtype=np.float64)
        mtprimeBTilde_tM_H1M0L = np.zeros(1, dtype=np.float64)
        mtprimeCTilde_tM_H1M0L = np.zeros(1, dtype=np.float64)
        mtprimeA_tM_H1M0L = np.zeros(1, dtype=np.float64)
        mtprimeB_tM_H1M0L = np.zeros(1, dtype=np.float64)
        mtprimeC_tM_H1M0L = np.zeros(1, dtype=np.float64)

        isRegionA_tM_ZB = np.zeros(1, dtype=int)
        isRegionB_tM_ZB = np.zeros(1, dtype=int)
        isRegionC_tM_ZB = np.zeros(1, dtype=int)
        isRegionD_tM_ZB = np.zeros(1, dtype=int)

        mtprimeATilde_tM_ZB = np.zeros(1, dtype=np.float64)
        mtprimeBTilde_tM_ZB = np.zeros(1, dtype=np.float64)
        mtprimeCTilde_tM_ZB = np.zeros(1, dtype=np.float64)
        mtprimeDTilde_tM_ZB = np.zeros(1, dtype=np.float64)

        mtprimeA_tM_ZB = np.zeros(1, dtype=np.float64)
        mtprimeB_tM_ZB = np.zeros(1, dtype=np.float64)
        mtprimeC_tM_ZB = np.zeros(1, dtype=np.float64)
        mtprimeD_tM_ZB = np.zeros(1, dtype=np.float64)

        newTree.Branch('pMassOld', pMassOld)
        newTree.Branch('pMassNew', pMassNew)

        newTree.Branch('ptTopTaggedM', ptTopTaggedM)
        newTree.Branch('etaTopTaggedM', etaTopTaggedM)
        newTree.Branch('phiTopTaggedM', phiTopTaggedM)
        newTree.Branch('MTopTaggedM', MTopTaggedM)
        newTree.Branch('sj0csvTopTaggedM', sj0csvTopTaggedM)
        newTree.Branch('sj1csvTopTaggedM', sj1csvTopTaggedM)
        newTree.Branch('tau32TopTaggedM', tau32TopTaggedM)

        newTree.Branch('ptTopTagged0M', ptTopTagged0M)
        newTree.Branch('etaTopTagged0M', etaTopTagged0M)
        newTree.Branch('phiTopTagged0M', phiTopTagged0M)
        newTree.Branch('MTopTagged0M', MTopTagged0M)
        newTree.Branch('sj0csvTopTagged0M', sj0csvTopTagged0M)
        newTree.Branch('sj1csvTopTagged0M', sj1csvTopTagged0M)
        newTree.Branch('tau32TopTagged0M', tau32TopTagged0M)

        newTree.Branch('ptHTagged1M1L', ptHTagged1M1L)
        newTree.Branch('etaHTagged1M1L', etaHTagged1M1L)
        newTree.Branch('phiHTagged1M1L', phiHTagged1M1L)
        newTree.Branch('MHTagged1M1L', MHTagged1M1L)
        newTree.Branch('sj0csvHTagged1M1L', sj0csvHTagged1M1L)
        newTree.Branch('sj1csvHTagged1M1L', sj1csvHTagged1M1L)
        newTree.Branch('tau21HTagged1M1L', tau21HTagged1M1L)

        newTree.Branch('ptHTagged1M0L', ptHTagged1M0L)
        newTree.Branch('etaHTagged1M0L', etaHTagged1M0L)
        newTree.Branch('phiHTagged1M0L', phiHTagged1M0L)
        newTree.Branch('MHTagged1M0L', MHTagged1M0L)
        newTree.Branch('sj0csvHTagged1M0L', sj0csvHTagged1M0L)
        newTree.Branch('sj1csvHTagged1M0L', sj1csvHTagged1M0L)
        newTree.Branch('tau21HTagged1M0L', tau21HTagged1M0L)

        newTree.Branch('ptZTagged1M1L', ptZTagged1M1L)
        newTree.Branch('etaZTagged1M1L', etaZTagged1M1L)
        newTree.Branch('phiZTagged1M1L', phiZTagged1M1L)
        newTree.Branch('MZTagged1M1L', MZTagged1M1L)
        newTree.Branch('sj0csvZTagged1M1L', sj0csvZTagged1M1L)
        newTree.Branch('sj1csvZTagged1M1L', sj1csvZTagged1M1L)
        newTree.Branch('tau21ZTagged1M1L', tau21ZTagged1M1L)

        newTree.Branch('ptZTagged0L', ptZTagged0L)
        newTree.Branch('etaZTagged0L', etaZTagged0L)
        newTree.Branch('phiZTagged0L', phiZTagged0L)
        newTree.Branch('MZTagged0L', MZTagged0L)
        newTree.Branch('sj0csvZTagged0L', sj0csvZTagged0L)
        newTree.Branch('sj1csvZTagged0L', sj1csvZTagged0L)
        newTree.Branch('tau21ZTagged0L', tau21ZTagged0L)

        newTree.Branch('mtprimeATilde', mtprimeATilde, 'mtprimeATilde/D')
        newTree.Branch('mtprimeBTilde', mtprimeBTilde, 'mtprimeBTilde/D')
        newTree.Branch('mtprimeCTilde', mtprimeCTilde, 'mtprimeCTilde/D')
        newTree.Branch('mtprimeDTilde', mtprimeDTilde, 'mtprimeDTilde/D')

        newTree.Branch('isRegionA_tM', isRegionA_tM, 'isRegionA_tM/I')
        newTree.Branch('isRegionB_tM', isRegionB_tM, 'isRegionB_tM/I')
        newTree.Branch('isRegionC_tM', isRegionC_tM, 'isRegionC_tM/I')
        newTree.Branch('isRegionD_tM', isRegionD_tM, 'isRegionD_tM/I')

        newTree.Branch('mtprimeATilde_tM', mtprimeATilde_tM, 'mtprimeATilde_tM/D')
        newTree.Branch('mtprimeBTilde_tM', mtprimeBTilde_tM, 'mtprimeBTilde_tM/D')
        newTree.Branch('mtprimeCTilde_tM', mtprimeCTilde_tM, 'mtprimeCTilde_tM/D')
        newTree.Branch('mtprimeDTilde_tM', mtprimeDTilde_tM, 'mtprimeDTilde_tM/D')

        newTree.Branch('mtprimeA_tM', mtprimeA_tM, 'mtprimeA_tM/D')
        newTree.Branch('mtprimeB_tM', mtprimeB_tM, 'mtprimeB_tM/D')
        newTree.Branch('mtprimeC_tM', mtprimeC_tM, 'mtprimeC_tM/D')
        newTree.Branch('mtprimeD_tM', mtprimeD_tM, 'mtprimeD_tM/D')
        newTree.Branch('isTopLeadingJet', isTopLeadingJet, 'isTopLeadingJet/I')
        newTree.Branch('isHiggsLeadingJet', isHiggsLeadingJet, 'isHiggsLeadingJet/I')
        newTree.Branch('higgsAnul', higgsAnul)
        newTree.Branch('ZAnul', ZAnul)
        newTree.Branch('isZLeadingJet', isZLeadingJet, 'isZLeadingJet/I')

        newTree.Branch('isRegionA_tM_H1M0L', isRegionA_tM_H1M0L, 'isRegionA_tM_H1M0L/I')
        newTree.Branch('isRegionB_tM_H1M0L', isRegionB_tM_H1M0L, 'isRegionB_tM_H1M0L/I')
        newTree.Branch('isRegionC_tM_H1M0L', isRegionC_tM_H1M0L, 'isRegionC_tM_H1M0L/I')

        newTree.Branch('mtprimeATilde_tM_H1M0L', mtprimeATilde_tM_H1M0L, 'mtprimeATilde_tM_H1M0L/D')
        newTree.Branch('mtprimeBTilde_tM_H1M0L', mtprimeBTilde_tM_H1M0L, 'mtprimeBTilde_tM_H1M0L/D')
        newTree.Branch('mtprimeCTilde_tM_H1M0L', mtprimeCTilde_tM_H1M0L, 'mtprimeCTilde_tM_H1M0L/D')

        newTree.Branch('mtprimeA_tM_H1M0L', mtprimeA_tM_H1M0L, 'mtprimeA_tM_H1M0L/D')
        newTree.Branch('mtprimeB_tM_H1M0L', mtprimeB_tM_H1M0L, 'mtprimeB_tM_H1M0L/D')
        newTree.Branch('mtprimeC_tM_H1M0L', mtprimeC_tM_H1M0L, 'mtprimeC_tM_H1M0L/D')

        newTree.Branch('isRegionD_tM_H1M0L', isRegionD_tM_H1M0L, 'isRegionD_tM_H1M0L/I')

        newTree.Branch('mtprimeDTilde_tM_H1M0L', mtprimeDTilde_tM_H1M0L, 'mtprimeDTilde_tM_H1M0L/D')

        newTree.Branch('mtprimeD_tM_H1M0L', mtprimeD_tM_H1M0L, 'mtprimeD_tM_H1M0L/D')

        newTree.Branch('isRegionA_tM_ZB', isRegionA_tM_ZB, 'isRegionA_tM_ZB/I')
        newTree.Branch('isRegionB_tM_ZB', isRegionB_tM_ZB, 'isRegionB_tM_ZB/I')
        newTree.Branch('isRegionC_tM_ZB', isRegionC_tM_ZB, 'isRegionC_tM_ZB/I')
        newTree.Branch('isRegionD_tM_ZB', isRegionD_tM_ZB, 'isRegionD_tM_ZB/I')

        newTree.Branch('mtprimeATilde_tM_ZB', mtprimeATilde_tM_ZB, 'mtprimeATilde_tM_ZB/D')
        newTree.Branch('mtprimeBTilde_tM_ZB', mtprimeBTilde_tM_ZB, 'mtprimeBTilde_tM_ZB/D')
        newTree.Branch('mtprimeCTilde_tM_ZB', mtprimeCTilde_tM_ZB, 'mtprimeCTilde_tM_ZB/D')
        newTree.Branch('mtprimeDTilde_tM_ZB', mtprimeDTilde_tM_ZB, 'mtprimeDTilde_tM_ZB/D')

        newTree.Branch('mtprimeA_tM_ZB', mtprimeA_tM_ZB, 'mtprimeA_tM_ZB/D')
        newTree.Branch('mtprimeB_tM_ZB', mtprimeB_tM_ZB, 'mtprimeB_tM_ZB/D')
        newTree.Branch('mtprimeC_tM_ZB', mtprimeC_tM_ZB, 'mtprimeC_tM_ZB/D')
        newTree.Branch('mtprimeD_tM_ZB', mtprimeD_tM_ZB, 'mtprimeD_tM_ZB/D')

        newTree.SetBranchAddress('SelectedEvent_btagsfZ', btZ)
        newTree.SetBranchAddress('SelectedEvent_btagsfZ_bcUp', btZbU)
        newTree.SetBranchAddress('SelectedEvent_btagsfZ_bcDown', btZbD)
        newTree.SetBranchAddress('SelectedEvent_btagsfZ_lUp', btZlU)
        newTree.SetBranchAddress('SelectedEvent_btagsfZ_lDown', btZlD)
        newTree.SetBranchAddress('SelectedEvent_btagsf' , bt)
        newTree.SetBranchAddress('SelectedEvent_btagsf_bcUp' , btbU)
        newTree.SetBranchAddress('SelectedEvent_btagsf_bcDown' , btbD)
        newTree.SetBranchAddress('SelectedEvent_btagsf_lUp' , btlU)
        newTree.SetBranchAddress('SelectedEvent_btagsf_lDown' , btlD)
        
        higgsLeadTruth = {}
        higgs2ndLeadTruth = {}
        ZLeadTruth = {}
        Z2ndLeadTruth = {}
        nEntries = oldTree.GetEntries()
        print 'processing: ', tree
        rand = rt.TRandom3()
        for iEvent in xrange(nEntries):
            if iEvent % 1000 == 0:
                print iEvent

            topIsLeading = False
            topIs2ndLeading = False
            top_MIsLeading = False
            top_MIs2ndLeading = False
            top0LIsLeading = False
            top0LIs2ndLeading = False
            top_0MIsLeading = False
            top_0MIs2ndLeading = False

            higgsLeadTruth[''] = False
            higgsLeadTruth['0L'] = False
            higgsLeadTruth['1M1L'] = False
            higgsLeadTruth['1M0L'] = False
            higgs2ndLeadTruth[''] = False
            higgs2ndLeadTruth['0L'] = False
            higgs2ndLeadTruth['1M1L'] = False
            higgs2ndLeadTruth['1M0L'] = False

            ZLeadTruth['2L'] = False
            ZLeadTruth['0L'] = False
            ZLeadTruth['noB'] = False
            ZLeadTruth['lowMass'] = False

            Z2ndLeadTruth['2L'] = False
            Z2ndLeadTruth['0L'] = False
            Z2ndLeadTruth['noB'] = False
            Z2ndLeadTruth['lowMass'] = False
            
            isA = False
            isB = False
            isC = False
            isD = False

            #clear vectors
            pMassOld.clear()
            pMassNew.clear()

            ptTopTaggedM.clear()
            etaTopTaggedM.clear()
            phiTopTaggedM.clear()
            MTopTaggedM.clear()
            tau32TopTaggedM.clear()
            sj0csvTopTaggedM.clear()
            sj1csvTopTaggedM.clear()

            ptTopTagged0M.clear()
            etaTopTagged0M.clear()
            phiTopTagged0M.clear()
            MTopTagged0M.clear()
            tau32TopTagged0M.clear()
            sj0csvTopTagged0M.clear()
            sj1csvTopTagged0M.clear()

            ptHTagged1M0L.clear()
            etaHTagged1M0L.clear()
            phiHTagged1M0L.clear()
            MHTagged1M0L.clear()
            tau21HTagged1M0L.clear()
            sj0csvHTagged1M0L.clear()
            sj1csvHTagged1M0L.clear()

            ptHTagged1M1L.clear()
            etaHTagged1M1L.clear()
            phiHTagged1M1L.clear()
            MHTagged1M1L.clear()
            tau21HTagged1M1L.clear()
            sj0csvHTagged1M1L.clear()
            sj1csvHTagged1M1L.clear()

            ptZTagged1M1L.clear()
            etaZTagged1M1L.clear()
            phiZTagged1M1L.clear()
            MZTagged1M1L.clear()
            tau21ZTagged1M1L.clear()
            sj0csvZTagged1M1L.clear()
            sj1csvZTagged1M1L.clear()

            ptZTagged0L.clear()
            etaZTagged0L.clear()
            phiZTagged0L.clear()
            MZTagged0L.clear()
            tau21ZTagged0L.clear()
            sj0csvZTagged0L.clear()
            sj1csvZTagged0L.clear()

            mtprimeATilde[0] = 0
            mtprimeBTilde[0] = 0
            mtprimeCTilde[0] = 0
            mtprimeDTilde[0] = 0

            mtprimeA_tM[0] = 0
            mtprimeB_tM[0] = 0
            mtprimeC_tM[0] = 0
            mtprimeD_tM[0] = 0
            mtprimeATilde_tM[0] = 0
            mtprimeBTilde_tM[0] = 0
            mtprimeCTilde_tM[0] = 0
            mtprimeDTilde_tM[0] = 0
            isRegionA_tM[0] = False
            isRegionB_tM[0] = False
            isRegionC_tM[0] = False
            isRegionD_tM[0] = False
            notABCD = False
            notABCD_tM = False
            notABCD_tM_H1M0L = False
            notABCD_tM_ZB = False
            isTopLeadingJet[0] = False
            isHiggsLeadingJet[0] = False
            isZLeadingJet[0] = False

            mtprimeD_tM_H1M0L[0] = 0
            mtprimeDTilde_tM_H1M0L[0] = 0
            isRegionD_tM_H1M0L[0] = False

            mtprimeA_tM_H1M0L[0] = 0
            mtprimeB_tM_H1M0L[0] = 0
            mtprimeC_tM_H1M0L[0] = 0
            mtprimeATilde_tM_H1M0L[0] = 0
            mtprimeBTilde_tM_H1M0L[0] = 0
            mtprimeCTilde_tM_H1M0L[0] = 0
            isRegionA_tM_H1M0L[0] = False
            isRegionB_tM_H1M0L[0] = False
            isRegionC_tM_H1M0L[0] = False
            notABCD_tM_H1M0L = False

            mtprimeA_tM_ZB[0] = 0
            mtprimeB_tM_ZB[0] = 0
            mtprimeC_tM_ZB[0] = 0
            mtprimeD_tM_ZB[0] = 0
            mtprimeATilde_tM_ZB[0] = 0
            mtprimeBTilde_tM_ZB[0] = 0
            mtprimeCTilde_tM_ZB[0] = 0
            mtprimeDTilde_tM_ZB[0] = 0
            isRegionA_tM_ZB[0] = False
            isRegionB_tM_ZB[0] = False
            isRegionC_tM_ZB[0] = False
            isRegionD_tM_ZB[0] = False

            oldTree.GetEntry(iEvent)

            isA = oldTree.isRegionA
            isB = oldTree.isRegionB
            isC = oldTree.isRegionC
            isD = oldTree.isRegionD
        
            if oldTree.ptAK8[0] < 400: continue
            #if (oldTree.ptAK8[0]+oldTree.ptAK8[1])<=850.: continue
            if oldTree.PrunedMassAK8[0] < 50.: continue

            if math.isnan(oldTree.btagsf):
               print 'btagsf is nan'
               bt[0] = 1.0
               btbU[0] = 1.0
               btbD[0] = 1.0
               btlU[0] = 1.0
               btlD[0] = 1.0
            else: 
               bt[0] = oldTree.btagsf
               btbU[0] = oldTree.btagsf_bcUp
               btbD[0] = oldTree.btagsf_bcDown
               btlU[0] = oldTree.btagsf_lUp
               btlD[0] = oldTree.btagsf_lDown
            if math.isnan(oldTree.btagsfZ):
               print 'btagsfZ is nan'
               btZ[0] = 1.0
               btZbU[0] = 1.0
               btZbD[0] = 1.0
               btZlU[0] = 1.0
               btZlD[0] = 1.0
            else: 
               btZ[0] = oldTree.btagsfZ
               btZbU[0] = oldTree.btagsfZ_bcUp
               btZbD[0] = oldTree.btagsfZ_bcDown
               btZlU[0] = oldTree.btagsfZ_lUp
               btZlD[0] = oldTree.btagsfZ_lDown
 
            for ijet in xrange(oldTree.ptAK8.size()):      
                pt = rt.Double(oldTree.ptAK8[ijet])
                eta = rt.Double(oldTree.etaAK8[ijet])
                phi = rt.Double(oldTree.phiAK8[ijet])
                mass = rt.Double(oldTree.MAK8[ijet])
                tau32 = rt.Double(oldTree.tau3AK8[ijet])/rt.Double(oldTree.tau2AK8[ijet])
                tau21 = rt.Double(oldTree.tau2AK8[ijet])/rt.Double(oldTree.tau1AK8[ijet])
                sdMass = rt.Double(oldTree.SoftDropMassAK8[ijet])
                pMass = rt.Double(oldTree.PrunedMassAK8[ijet])
                sj0csv = rt.Double(oldTree.sj0CSVAK8[ijet])
                sj1csv = rt.Double(oldTree.sj1CSVAK8[ijet])
                sjMaxCSV = rt.TMath.Max(sj0csv,sj1csv)

#----------------------------------------------------------------------------------------------------------------------------
#                                                             top
#----------------------------------------------------------------------------------------------------------------------------
                #massSmear = 1.0
                #rand = rt.TRandom3()
                #scaleMass = 1.16
                #if 'JER' in tree and 'Up' in tree:
                #    scaleMass += 0.077
                #elif 'JER' in tree and 'Down' in tree:
                #    scaleMass -= 0.077
                #if 'JetHT' not in inputFile:
                #    massSmear = 1 + rand.Gaus(0.,0.1)*math.sqrt(max(scaleMass*scaleMass - 1., 0.))
                #pMassOld.push_back(pMass)
                #pMass = massSmear * pMass
                #pMassNew.push_back(pMass)

                if pt>400. and 105.<=sdMass<220. and tau32<tag0p3 and sjMaxCSV>=CSVv2M:
                    ptTopTaggedM.push_back(pt)
                    etaTopTaggedM.push_back(eta)
                    phiTopTaggedM.push_back(phi)
                    MTopTaggedM.push_back(mass)
                    tau32TopTaggedM.push_back(tau32)
                    sj0csvTopTaggedM.push_back(sj0csv)
                    sj1csvTopTaggedM.push_back(sj1csv)

                    if ijet == 0:
                        top_MIsLeading = True
                        p4Top1_M = rt.TLorentzVector()
                        p4Top1_M.SetPtEtaPhiM(oldTree.ptAK8[0],oldTree.etaAK8[0],oldTree.phiAK8[0],oldTree.MAK8[0])
                    if ijet == 1:
                        top_MIs2ndLeading = True
                        p4Top2_M = rt.TLorentzVector()
                        p4Top2_M.SetPtEtaPhiM(oldTree.ptAK8[1],oldTree.etaAK8[1],oldTree.phiAK8[1],oldTree.MAK8[1])
                    if top_MIsLeading or top_MIs2ndLeading: isTopLeadingJet[0] = True

                if pt>400. and 105.<=sdMass<220. and tau32<tag0p3 and sjMaxCSV<CSVv2M:
                    ptTopTagged0M.push_back(pt)
                    etaTopTagged0M.push_back(eta)
                    phiTopTagged0M.push_back(phi)
                    MTopTagged0M.push_back(mass)
                    tau32TopTagged0M.push_back(tau32)
                    sj0csvTopTagged0M.push_back(sj0csv)
                    sj1csvTopTagged0M.push_back(sj1csv)

                    if ijet == 0:
                        top_0MIsLeading = True
                        p4Top1_0M = rt.TLorentzVector()
                        p4Top1_0M.SetPtEtaPhiM(oldTree.ptAK8[0],oldTree.etaAK8[0],oldTree.phiAK8[0],oldTree.MAK8[0])
                    if ijet == 1:
                        top_0MIs2ndLeading = True
                        p4Top2_0M = rt.TLorentzVector()
                        p4Top2_0M.SetPtEtaPhiM(oldTree.ptAK8[1],oldTree.etaAK8[1],oldTree.phiAK8[1],oldTree.MAK8[1])
 
                if pt>400. and 105.<=sdMass<220. and tau32<tag0p1 and sjMaxCSV>=CSVv2L:
                    if ijet == 0:
                        topIsLeading = True
                        p4Top1 = rt.TLorentzVector()
                        p4Top1.SetPtEtaPhiM(oldTree.ptAK8[0],oldTree.etaAK8[0],oldTree.phiAK8[0],oldTree.MAK8[0])
                    if ijet == 1:
                        topIs2ndLeading = True
                        p4Top2 = rt.TLorentzVector()
                        p4Top2.SetPtEtaPhiM(oldTree.ptAK8[1],oldTree.etaAK8[1],oldTree.phiAK8[1],oldTree.MAK8[1])
 
                if pt>400. and 105.<=sdMass<220. and tau32<tag0p1 and sjMaxCSV<CSVv2L:
                    if ijet == 0:
                        top0LIsLeading = True
                        p4Top1_0L = rt.TLorentzVector()
                        p4Top1_0L.SetPtEtaPhiM(oldTree.ptAK8[0],oldTree.etaAK8[0],oldTree.phiAK8[0],oldTree.MAK8[0])
                    if ijet == 1:
                        top0LIs2ndLeading = True
                        p4Top2_0L = rt.TLorentzVector()
                        p4Top2_0L.SetPtEtaPhiM(oldTree.ptAK8[1],oldTree.etaAK8[1],oldTree.phiAK8[1],oldTree.MAK8[1])
#----------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------
#                                                             Higgs
#----------------------------------------------------------------------------------------------------------------------------
                if pt>300. and 105.<=pMass<135. and tau21<0.6 and ((sj0csv>=CSVv2L and sj1csv>=CSVv2M) or (sj0csv>=CSVv2M and sj1csv>=CSVv2L)):
                    ptHTagged1M1L.push_back(pt)
                    etaHTagged1M1L.push_back(eta)
                    phiHTagged1M1L.push_back(phi)
                    MHTagged1M1L.push_back(mass)
                    tau21HTagged1M1L.push_back(tau21)
                    sj0csvHTagged1M1L.push_back(sj0csv)
                    sj1csvHTagged1M1L.push_back(sj1csv)

                    if ijet == 0:
                        higgsLeadTruth['1M1L'] = True
                        p4H1_1M1L = rt.TLorentzVector()
                        p4H1_1M1L.SetPtEtaPhiM(oldTree.ptAK8[0],oldTree.etaAK8[0],oldTree.phiAK8[0],oldTree.MAK8[0])

                    if ijet == 1:
                        higgs2ndLeadTruth['1M1L'] = True
                        p4H2_1M1L = rt.TLorentzVector()
                        p4H2_1M1L.SetPtEtaPhiM(oldTree.ptAK8[1],oldTree.etaAK8[1],oldTree.phiAK8[1],oldTree.MAK8[1])

                    if higgsLeadTruth['1M1L'] or higgs2ndLeadTruth['1M1L']: 
                        isHiggsLeadingJet[0] = True
                        

                if pt>300. and 105.<=pMass<135. and tau21<0.6 and ((sj0csv>=CSVv2M and sj1csv<CSVv2L) or (sj0csv<CSVv2L and sj1csv>=CSVv2M)):
                    ptHTagged1M0L.push_back(pt)
                    etaHTagged1M0L.push_back(eta)
                    phiHTagged1M0L.push_back(phi)
                    MHTagged1M0L.push_back(mass)
                    tau21HTagged1M0L.push_back(tau21)
                    sj0csvHTagged1M0L.push_back(sj0csv)
                    sj1csvHTagged1M0L.push_back(sj1csv)

                    if ijet == 0:
                        higgsLeadTruth['1M0L'] = True
                        p4H1_1M0L = rt.TLorentzVector()
                        p4H1_1M0L.SetPtEtaPhiM(oldTree.ptAK8[0],oldTree.etaAK8[0],oldTree.phiAK8[0],oldTree.MAK8[0])
                    if ijet == 1:
                        higgs2ndLeadTruth['1M0L'] = True
                        p4H2_1M0L = rt.TLorentzVector()
                        p4H2_1M0L.SetPtEtaPhiM(oldTree.ptAK8[1],oldTree.etaAK8[1],oldTree.phiAK8[1],oldTree.MAK8[1])

                if pt>300. and 105.<=pMass<135. and tau21<0.6 and sj0csv>=CSVv2L and sj1csv>=CSVv2L:
                    if ijet == 0:
                        higgsLeadTruth[''] = True
                        p4H1 = rt.TLorentzVector()
                        p4H1.SetPtEtaPhiM(oldTree.ptAK8[0],oldTree.etaAK8[0],oldTree.phiAK8[0],oldTree.MAK8[0])
                    if ijet == 1:
                        higgs2ndLeadTruth[''] = True
                        p4H2 = rt.TLorentzVector()
                        p4H2.SetPtEtaPhiM(oldTree.ptAK8[1],oldTree.etaAK8[1],oldTree.phiAK8[1],oldTree.MAK8[1])

                if pt>300. and 105.<=pMass<135. and tau21<0.6 and sj0csv<CSVv2L and sj1csv<CSVv2L:
                    if ijet == 0:
                        higgsLeadTruth['0L'] = True
                        p4H1_0L = rt.TLorentzVector()
                        p4H1_0L.SetPtEtaPhiM(oldTree.ptAK8[0],oldTree.etaAK8[0],oldTree.phiAK8[0],oldTree.MAK8[0])
                    if ijet == 1:
                        higgs2ndLeadTruth['0L'] = True
                        p4H2_0L = rt.TLorentzVector()
                        p4H2_0L.SetPtEtaPhiM(oldTree.ptAK8[1],oldTree.etaAK8[1],oldTree.phiAK8[1],oldTree.MAK8[1])
#----------------------------------------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------
#                                                             Z
#----------------------------------------------------------------------------------------------------------------------------

                if pt>200. and 65.<=pMass<105. and tau21<0.6 and ((sj0csv>=CSVv2L and sj1csv>=CSVv2L) and (sj0csv>=CSVv2M or sj1csv>=CSVv2M)):
                    ptZTagged1M1L.push_back(pt)
                    etaZTagged1M1L.push_back(eta)
                    phiZTagged1M1L.push_back(phi)
                    MZTagged1M1L.push_back(mass)
                    tau21ZTagged1M1L.push_back(tau21)
                    sj0csvZTagged1M1L.push_back(sj0csv)
                    sj1csvZTagged1M1L.push_back(sj1csv)

                    if ijet == 0:
                        ZLeadTruth['2L'] = True
                        p4Z1 = rt.TLorentzVector()
                        p4Z1.SetPtEtaPhiM(oldTree.ptAK8[0],oldTree.etaAK8[0],oldTree.phiAK8[0],oldTree.MAK8[0])
                    if ijet == 1:
                        Z2ndLeadTruth['2L'] = True
                        p4Z2 = rt.TLorentzVector()
                        p4Z2.SetPtEtaPhiM(oldTree.ptAK8[1],oldTree.etaAK8[1],oldTree.phiAK8[1],oldTree.MAK8[1])
                    if ZLeadTruth['2L'] or Z2ndLeadTruth['2L']: isZLeadingJet[0] = True

                if pt>200. and 65.<=pMass<105. and tau21<0.6 and sj0csv<CSVv2L and sj1csv<CSVv2L:
                    ptZTagged0L.push_back(pt)
                    etaZTagged0L.push_back(eta)
                    phiZTagged0L.push_back(phi)
                    MZTagged0L.push_back(mass)
                    tau21ZTagged0L.push_back(tau21)
                    sj0csvZTagged0L.push_back(sj0csv)
                    sj1csvZTagged0L.push_back(sj1csv)
                    if ijet == 0:
                        ZLeadTruth['0L'] = True
                        p4Z1_0L = rt.TLorentzVector()
                        p4Z1_0L.SetPtEtaPhiM(oldTree.ptAK8[0],oldTree.etaAK8[0],oldTree.phiAK8[0],oldTree.MAK8[0])
                    if ijet == 1:
                        Z2ndLeadTruth['0L'] = True
                        p4Z2_0L = rt.TLorentzVector()
                        p4Z2_0L.SetPtEtaPhiM(oldTree.ptAK8[1],oldTree.etaAK8[1],oldTree.phiAK8[1],oldTree.MAK8[1])




#----------------------------------------------------------------------------------------------------------------------------

            if top_MIsLeading and higgs2ndLeadTruth['']: 
                isRegionD_tM[0] = True
                top_M = p4Top1_M
                higgs = p4H2
            elif top_MIs2ndLeading and higgsLeadTruth['']: 
                isRegionD_tM[0] = True
                top_M = p4Top2_M
                higgs = p4H1
            elif top_MIsLeading and higgs2ndLeadTruth['0L']: 
                isRegionB_tM[0] = True
                top_M = p4Top1_M
                higgs_0L = p4H2_0L
            elif top_MIs2ndLeading and higgsLeadTruth['0L']: 
                isRegionB_tM[0] = True
                top_M = p4Top2_M
                higgs_0L = p4H1_0L
            elif top_0MIsLeading and higgs2ndLeadTruth['']:
                isRegionC_tM[0] = True
                top_0M = p4Top1_0M
                higgs = p4H2
            elif top_0MIs2ndLeading and higgsLeadTruth['']: 
                isRegionC_tM[0] = True
                top_0M = p4Top2_0M
                higgs = p4H1
            elif top_0MIsLeading and higgs2ndLeadTruth['0L']: 
                isRegionA_tM[0] = True
                top_0M = p4Top1_0M
                higgs_0L = p4H2_0L
            elif top_0MIs2ndLeading and higgsLeadTruth['0L']: 
                isRegionA_tM[0] = True
                top_0M = p4Top2_0M
                higgs_0L = p4H1_0L
            else: notABCD_tM = True

            if top_MIsLeading and higgs2ndLeadTruth['1M1L']: 
                isRegionD_tM_H1M0L[0] = True
                top_M = p4Top1_M
                higgs_1M1L = p4H2_1M1L
            elif top_MIs2ndLeading and higgsLeadTruth['1M1L']: 
                isRegionD_tM_H1M0L[0] = True
                top_M = p4Top2_M
                higgs_1M1L = p4H1_1M1L

            if not isRegionD_tM_H1M0L[0]:
                if top_MIsLeading and higgs2ndLeadTruth['1M0L']:
                    isRegionB_tM_H1M0L[0] = True
                    top_M = p4Top1_M
                    higgs_1M0L = p4H2_1M0L
                elif top_MIs2ndLeading and higgsLeadTruth['1M0L']: 
                    isRegionB_tM_H1M0L[0] = True
                    top_M = p4Top2_M
                    higgs_1M0L = p4H1_1M0L
            if not isRegionD_tM_H1M0L[0] and not isRegionB_tM_H1M0L[0]:
                if top_0MIsLeading and higgs2ndLeadTruth['1M1L']:
                    isRegionC_tM_H1M0L[0] = True
                    top_0M = p4Top1_0M
                    higgs_1M0L = p4H2_1M1L
                elif top_0MIs2ndLeading and higgsLeadTruth['1M1L']: 
                    isRegionC_tM_H1M0L[0] = True
                    top_0M = p4Top2_0M
                    higgs_1M0L = p4H1_1M1L
            if not isRegionD_tM_H1M0L[0] and not isRegionB_tM_H1M0L[0] and not isRegionC_tM_H1M0L[0]:
                if top_0MIsLeading and higgs2ndLeadTruth['1M0L']: 
                    isRegionA_tM_H1M0L[0] = True
                    top_0M = p4Top1_0M
                    higgs_1M0L = p4H2_1M0L
                elif top_0MIs2ndLeading and higgsLeadTruth['1M0L']: 
                    isRegionA_tM_H1M0L[0] = True
                    top_0M = p4Top2_0M
                    higgs_1M0L = p4H1_1M0L
                else: notABCD_tM_H1M0L = True

            if notABCD_tM_H1M0L:
                if top_MIsLeading and Z2ndLeadTruth['2L']: 
                    isRegionD_tM_ZB[0] = True
                    top_M = p4Top1_M
                    Z = p4Z2
                elif top_MIs2ndLeading and ZLeadTruth['2L']: 
                    isRegionD_tM_ZB[0] = True
                    top_M = p4Top2_M
                    Z = p4Z1
                elif top_MIsLeading and Z2ndLeadTruth['0L']: 
                    isRegionB_tM_ZB[0] = True
                    top_M = p4Top1_M
                    Z_0L = p4Z2_0L
                elif top_MIs2ndLeading and ZLeadTruth['0L']: 
                    isRegionB_tM_ZB[0] = True
                    top_M = p4Top2_M
                    Z_0L = p4Z1_0L
                elif top_0MIsLeading and Z2ndLeadTruth['2L']:
                    isRegionC_tM_ZB[0] = True
                    top_0M = p4Top1_0M
                    Z = p4Z2
                elif top_0MIs2ndLeading and ZLeadTruth['2L']: 
                    isRegionC_tM_ZB[0] = True
                    top_0M = p4Top2_0M
                    Z = p4Z1
                elif top_0MIsLeading and Z2ndLeadTruth['0L']: 
                    isRegionA_tM_ZB[0] = True
                    top_0M = p4Top1_0M
                    Z_0L = p4Z2_0L
                elif top_0MIs2ndLeading and ZLeadTruth['0L']: 
                    isRegionA_tM_ZB[0] = True
                    top_0M = p4Top2_0M
                    Z_0L = p4Z1_0L
                else: notABCD_tM_ZB = True

            if isA:
                if top0LIsLeading and higgs2ndLeadTruth['0L']:
                    top0L = p4Top1_0L
                    higgs_0L = p4H2_0L
                    mtprimeATilde[0] = (top0L+higgs_0L).M() - top0L.M() - higgs_0L.M() + 172.5 + 125           
                elif top0LIs2ndLeading and higgsLeadTruth['0L']:
                    top0L = p4Top2_0L
                    higgs_0L = p4H1_0L
                    mtprimeATilde[0] = (top0L+higgs_0L).M() - top0L.M() - higgs_0L.M() + 172.5 + 125           
            if isB:
                if topIsLeading and higgs2ndLeadTruth['0L']:
                    top = p4Top1
                    higgs_0L = p4H2_0L
                    mtprimeBTilde[0] = (top+higgs_0L).M() - top.M() - higgs_0L.M() + 172.5 + 125           
                elif topIs2ndLeading and higgsLeadTruth['0L']:
                    top = p4Top2
                    higgs_0L = p4H1_0L
                    mtprimeBTilde[0] = (top+higgs_0L).M() - top.M() - higgs_0L.M() + 172.5 + 125           
            if isC:
                if top0LIsLeading and higgs2ndLeadTruth['']:
                    top0L = p4Top1_0L
                    higgs = p4H2
                    mtprimeCTilde[0] = (top0L+higgs).M() - top0L.M() - higgs.M() + 172.5 + 125           
                elif top0LIs2ndLeading and higgsLeadTruth['']:
                    top0L = p4Top2_0L
                    higgs = p4H1
                    mtprimeCTilde[0] = (top0L+higgs).M() - top0L.M() - higgs.M() + 172.5 + 125           
            if isD:
                if topIsLeading and higgs2ndLeadTruth['']:
                    top = p4Top1
                    higgs = p4H2
                    mtprimeDTilde[0] = (top+higgs).M() - top.M() - higgs.M() + 172.5 + 125           
                elif topIs2ndLeading and higgsLeadTruth['']:
                    top = p4Top2
                    higgs = p4H1
                    mtprimeDTilde[0] = (top+higgs).M() - top.M() - higgs.M() + 172.5 + 125           

            if isRegionA_tM[0]:
                mtprimeATilde_tM[0] = (top_0M+higgs_0L).M() - top_0M.M() - higgs_0L.M() + 172.5 + 125           
                mtprimeA_tM[0] = (top_0M+higgs_0L).M()          
            if isRegionB_tM[0]:
                mtprimeBTilde_tM[0] = (top_M+higgs_0L).M() - top_M.M() - higgs_0L.M() + 172.5 + 125           
                mtprimeB_tM[0] = (top_M+higgs_0L).M()          
            if isRegionC_tM[0]:
                mtprimeCTilde_tM[0] = (top_0M+higgs).M() - top_0M.M() - higgs.M() + 172.5 + 125           
                mtprimeC_tM[0] = (top_0M+higgs).M()          
            if isRegionD_tM[0]:
                mtprimeDTilde_tM[0] = (top_M+higgs).M() - top_M.M() - higgs.M() + 172.5 + 125           
                mtprimeD_tM[0] = (top_M+higgs).M()          
 
            if isRegionD_tM_H1M0L[0]:
                mtprimeDTilde_tM_H1M0L[0] = (top_M+higgs_1M1L).M() - top_M.M() - higgs_1M1L.M() + 172.5 + 125           
                mtprimeD_tM_H1M0L[0] = (top_M+higgs_1M1L).M()         
 
            if isRegionA_tM_H1M0L[0]:
                mtprimeATilde_tM_H1M0L[0] = (top_0M+higgs_1M0L).M() - top_0M.M() - higgs_1M0L.M() + 172.5 + 125           
                mtprimeA_tM_H1M0L[0] = (top_0M+higgs_1M0L).M()          
            if isRegionB_tM_H1M0L[0]:
                mtprimeBTilde_tM_H1M0L[0] = (top_M+higgs_1M0L).M() - top_M.M() - higgs_1M0L.M() + 172.5 + 125           
                mtprimeB_tM_H1M0L[0] = (top_M+higgs_1M0L).M()          
            if isRegionC_tM_H1M0L[0]:
                mtprimeCTilde_tM_H1M0L[0] = (top_0M+higgs_1M0L).M() - top_0M.M() - higgs_1M0L.M() + 172.5 + 125           
                mtprimeC_tM_H1M0L[0] = (top_0M+higgs_1M0L).M()          

            if isRegionA_tM_ZB[0]:
                mtprimeATilde_tM_ZB[0] = (top_0M+Z_0L).M() - top_0M.M() - Z_0L.M() + 172.5 + 91           
                mtprimeA_tM_ZB[0] = (top_0M+Z_0L).M()          
            if isRegionB_tM_ZB[0]:
                mtprimeBTilde_tM_ZB[0] = (top_M+Z_0L).M() - top_M.M() - Z_0L.M() + 172.5 + 91           
                mtprimeB_tM_ZB[0] = (top_M+Z_0L).M()          
            if isRegionC_tM_ZB[0]:
                mtprimeCTilde_tM_ZB[0] = (top_0M+Z).M() - top_0M.M() - Z.M() + 172.5 + 91           
                mtprimeC_tM_ZB[0] = (top_0M+Z).M()          
            if isRegionD_tM_ZB[0]:
                mtprimeDTilde_tM_ZB[0] = (top_M+Z).M() - top_M.M() - Z.M() + 172.5 + 91           
                mtprimeD_tM_ZB[0] = (top_M+Z).M()          

            higgsAnul[0] = False 
            higgsAnul[1] = False 
            higgsAnul[2] = False 
            higgsAnul[3] = False 
            higgsAnul[4] = False 
            higgsAnul[5] = False 
            higgsAnul[6] = False 
            higgsAnul[7] = False 
            higgsAnul[8] = False
            if  isRegionD_tM_H1M0L[0] or isRegionC_tM_H1M0L[0] or isRegionA_tM_H1M0L[0] or isRegionB_tM_H1M0L[0]:
                if isRegionD_tM_H1M0L[0]:
                    higgs_dR = higgs_1M1L
                elif isRegionC_tM_H1M0L[0]:
                    higgs_dR = higgs_1M0L
                elif isRegionA_tM_H1M0L[0]:
                    higgs_dR = higgs_1M0L
                elif isRegionB_tM_H1M0L[0]:
                    higgs_dR = higgs_1M0L
                for ijet in xrange(oldTree.ptAK4.size()):
                    ak4P4 = rt.TLorentzVector()
                    ak4P4.SetPtEtaPhiM(oldTree.ptAK4[ijet],oldTree.etaAK4[ijet],oldTree.phiAK4[ijet],oldTree.MAK4[ijet])
                    deltaR = higgs_dR.DeltaR(ak4P4)
                    if 0.55 <= deltaR <= 0.8:  higgsAnul[0] = True
                    if 0.55 <= deltaR <= 0.85: higgsAnul[1] = True
                    if 0.55 <= deltaR <= 0.9:  higgsAnul[2] = True
                    if 0.6  <= deltaR <= 0.8:  higgsAnul[3] = True
                    if 0.6  <= deltaR <= 0.85: higgsAnul[4] = True
                    if 0.6  <= deltaR <= 0.9:  higgsAnul[5] = True
                    if 0.65 <= deltaR <= 0.8:  higgsAnul[6] = True
                    if 0.65 <= deltaR <= 0.85: higgsAnul[7] = True
                    if 0.65 <= deltaR <= 0.9:  higgsAnul[8] = True

            ZAnul[0] = False 
            ZAnul[1] = False 
            ZAnul[2] = False 
            ZAnul[3] = False 
            ZAnul[4] = False 
            ZAnul[5] = False 
            ZAnul[6] = False 
            ZAnul[7] = False 
            ZAnul[8] = False
            if  isRegionD_tM_ZB[0] or isRegionC_tM_ZB[0] or isRegionA_tM_ZB[0] or isRegionB_tM_ZB[0]:
                if isRegionD_tM_ZB[0] or isRegionC_tM_ZB[0]:
                    Z_dR = Z
                else:
                    Z_dR = Z_0L
                for ijet in xrange(oldTree.ptAK4.size()):
                    ak4P4 = rt.TLorentzVector()
                    ak4P4.SetPtEtaPhiM(oldTree.ptAK4[ijet],oldTree.etaAK4[ijet],oldTree.phiAK4[ijet],oldTree.MAK4[ijet])
                    deltaR = Z_dR.DeltaR(ak4P4)
                    if 0.55 <= deltaR <= 0.8:  ZAnul[0] = True
                    if 0.55 <= deltaR <= 0.85: ZAnul[1] = True
                    if 0.55 <= deltaR <= 0.9:  ZAnul[2] = True
                    if 0.6  <= deltaR <= 0.8:  ZAnul[3] = True
                    if 0.6  <= deltaR <= 0.85: ZAnul[4] = True
                    if 0.6  <= deltaR <= 0.9:  ZAnul[5] = True
                    if 0.65 <= deltaR <= 0.8:  ZAnul[6] = True
                    if 0.65 <= deltaR <= 0.85: ZAnul[7] = True
                    if 0.65 <= deltaR <= 0.9:  ZAnul[8] = True

            if not isA and not isB and not isC and not isD: notABCD = True
            #if notABCD and notABCD_tM_H1M0L and notABCD_tM_ZB: continue 
            newTree.Fill()
        newTree.AutoSave()

if __name__ == "__main__":
    ifile = sys.argv[1]
    ofile = sys.argv[2]
    sw = rt.TStopwatch()
    sw.Start()
    reduceTree(['CHS'], ifile, ofile)
    #reduceTree(['CHS','JERUp','JERDown','JESUp','JESDown'], ifile, ofile)
    #reduceTree(['CHS'], 'samples_v2p4_sys/TbtZ_1800_RH.root', './samples_reduced/samples_v2p4_sys_v2/TbtZ_1800_RH_reduced.root')
    #reduceTree(['CHS'], 'samples_v2p4_sys/TbtZ_1200_RH.root', './samples_reduced/samples_v2p4_sys_v2/TbtZ_1200_RH_reduced.root')
    #reduceTree(['CHS'], '../samples_v2p4_sys/TTJets.root', '../samples_reduced/samples_v2p4_sys_v2/TTJets_reduced.root')
    sw.Stop()
    sw.Print()
    #reduceTree(['CHS'], 'samples_v2p4_sys/TbtH_1200_LH.root', './test.root')
