// -*- C++ -*-
//
// Package:    UserCode/TprimeAna
// Class:      TprimeAna
// 
/**\class TprimeAna TprimeAna.cc UserCode/TprimeAna/plugins/TprimeAna.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Robert Stringer
//         Created:  Fri, 20 Feb 2015 19:13:03 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include <TLorentzVector.h>
#include <string>
#include <iostream>
#include "AnalysisDataFormats/BoostedObjects/interface/GenParticleWithDaughters.h"
#include <TH2F.h>
#include <TTree.h>

using namespace std;

//
// class declaration
//

class TprimeAna : public edm::EDAnalyzer {
   public:
      explicit TprimeAna(const edm::ParameterSet&);
      ~TprimeAna();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      bool _isData;
      edm::InputTag l_trigName;
      edm::InputTag l_trigBit;
      std::vector<std::string> hltPaths_           ;


      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
      //

      edm::Service<TFileService> fs;
      std::map< std::string, TH1F* > histos;
      std::map< std::string, TH2F* > histos2;
	
      TTree * cutTree;

        bool bx2AK8Jets , b2AK8Jets, b6AK4Jets , b2AK4Jets , b1AK4Jets, bTMass , bHMass , bHTag , bTTag, bTTagSubj,
             bLoose1 ,bMedium1 , bTight1;

        double softDropMassLeadAK8; 
        double trimmedMassLeadAK8; 
        double ptLeadingAK4,pt2ndAK4,pt3rdAK4,pt4thAK4,pt5thAK4,pt6thAK4;
        double etaLeadingAK4,eta2ndAK4,eta3rdAK4,eta4thAK4,eta5thAK4,eta6thAK4;
	double massTprime;

        bool bAK4LeadingPt; 
        bool bMass2AK8_1200;
        bool bMass2AK8_1700; 
        bool bSoftDropMassAK8; 
        bool bTrimmedMassAK8; 
	
        std::vector<bool> * bTrigger;

	std::vector<double> * ptAK8;
	std::vector<double> * etaAK8;
	std::vector<unsigned> * AK8Idx;

	std::vector<double> * EvtWeight;

	std::vector<unsigned> * idxHTag;
	std::vector<unsigned> * idxTTag;
	std::vector<unsigned> * idxWTag;
	std::vector<unsigned> * idxbTag;

	std::vector<unsigned> * subjAK8;

	unsigned nAK8;

        bool brelM;
        // Rel Pt

        double relM, relpt;
        bool brelpt; 
        bool bForwardJet;
        unsigned looseBTag, mediumBTag, tightBTag;

	double htak4, fMaxEtaAK4;
};
//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
TprimeAna::TprimeAna(const edm::ParameterSet& iConfig):
	_isData                 (iConfig.getParameter<bool>              ("isData")),
  	l_trigName              (iConfig.getParameter<edm::InputTag>     ("trigNameLabel")),
  	l_trigBit               (iConfig.getParameter<edm::InputTag>     ("trigBitLabel")),
        hltPaths_               (iConfig.getParameter<vector<string>>    ("hltPaths"))

{
   //now do what ever initialization is needed
 

}


TprimeAna::~TprimeAna()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
TprimeAna::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
   using namespace edm;
   using namespace vlq;

#ifdef THIS_IS_AN_EVENT_EXAMPLE
   Handle<ExampleData> pIn;
   iEvent.getByLabel("example",pIn);
#endif
   
#ifdef THIS_IS_AN_EVENTSETUP_EXAMPLE
   ESHandle<SetupData> pSetup;
   iSetup.get<SetupRecord>().get(pSetup);

   
#endif



      edm::Handle<ULong64_t> mh_evtNum;

      edm::Handle<std::vector<float> > mh_elPt;
      edm::Handle<std::vector<float> > mh_elEta;
      edm::Handle<std::vector<float> > mh_elPhi;
      edm::Handle<std::vector<float> > mh_elE;
      edm::Handle<std::vector<float> > mh_elCharge;
      edm::Handle<std::vector<float> > mh_elisMedium;

      edm::Handle<std::vector<float> > mh_muPt;
      edm::Handle<std::vector<float> > mh_muEta;
      edm::Handle<std::vector<float> > mh_muPhi;
      edm::Handle<std::vector<float> > mh_muE;
      edm::Handle<std::vector<float> > mh_muCharge;
      edm::Handle<std::vector<float> > mh_muIsTightMuon;

      edm::Handle<std::vector<float> > mh_jetAK4Pt;
      edm::Handle<std::vector<float> > mh_jetAK4GenPartonPt;
      edm::Handle<std::vector<float> > mh_jetAK4Eta;
      edm::Handle<std::vector<float> > mh_jetAK4GenPartonY;
      edm::Handle<std::vector<float> > mh_jetAK4Phi;
      edm::Handle<std::vector<float> > mh_jetAK4E;
      edm::Handle<std::vector<float> > mh_jetAK4HadronFlavour;
      edm::Handle<std::vector<float> > mh_jetAK4CSV;
      edm::Handle<std::vector<float> > mh_jetAK4Mass;
      edm::Handle<std::vector<unsigned> > mh_jetAK4Good;
      edm::Handle<double> mh_htak4jets;
      edm::Handle<double> mh_htak4trigjets;
      edm::Handle<double> mh_htak8jets;

      edm::Handle<std::vector<float> > mh_jetAK8Pt;
      edm::Handle<std::vector<float> > mh_jetAK8Eta;
      edm::Handle<std::vector<float> > mh_jetAK8Phi;
      edm::Handle<std::vector<float> > mh_jetAK8E;
      edm::Handle<std::vector<float> > mh_jetAK8Mass;
      edm::Handle<std::vector<float> > mh_jetAK8subjetIndex0;
      edm::Handle<std::vector<float> > mh_jetAK8subjetIndex1;
      edm::Handle<std::vector<float> > mh_jetAK8HadronFlavour;
      edm::Handle<std::vector<float> > mh_jetAK8tau1;
      edm::Handle<std::vector<float> > mh_jetAK8tau2;
      edm::Handle<std::vector<float> > mh_jetAK8tau3;
      edm::Handle<std::vector<unsigned> > mh_jetAK8Good; 
      edm::Handle<std::vector<float> > mh_jetAK8nSubjets;

      edm::Handle<std::vector<float> >  mh_jetAK8FilteredMass;
      edm::Handle<std::vector<float> >  mh_jetAK8TrimmedMass    ;
      edm::Handle<std::vector<float> >  mh_jetAK8PrunedMass     ;
      edm::Handle<std::vector<float> >  mh_jetAK8SoftDropMass   ; 

      edm::Handle<std::vector<float> > mh_subjetAK8Pt;
      edm::Handle<std::vector<float> > mh_subjetAK8Eta;
      edm::Handle<std::vector<float> > mh_subjetAK8Phi;
      edm::Handle<std::vector<float> > mh_subjetAK8E;
      edm::Handle<std::vector<float> > mh_subjetAK8Mass;
      edm::Handle<std::vector<float> > mh_subjetAK8HadronFlavour;
      edm::Handle<std::vector<float> > mh_subjetAK8CSV;

      edm::Handle<std::vector<float> > mh_jetsCmsTopTagPt;
      edm::Handle<std::vector<float> > mh_jetsCmsTopTagEta;
      edm::Handle<std::vector<float> > mh_jetsCmsTopTagPhi;
      edm::Handle<std::vector<float> > mh_jetsCmsTopTagE;
      edm::Handle<std::vector<float> > mh_jetsCmsTopTagMass;
      edm::Handle<std::vector<float> > mh_jetsCmsTopTagsubjetIndex0;
      edm::Handle<std::vector<float> > mh_jetsCmsTopTagsubjetIndex1;
      edm::Handle<std::vector<float> > mh_jetsCmsTopTagHadronFlavour;
      edm::Handle<std::vector<float> > mh_jetsCmsTopTagtau1;
      edm::Handle<std::vector<float> > mh_jetsCmsTopTagtau2;
      edm::Handle<std::vector<float> > mh_jetsCmsTopTagtau3;

      edm::Handle<std::vector<float> > mh_subjetAK8CSVV1;
//      edm::Handle<GenParticlesWithDaughtersCollection> mh_hbbCandidates;

      edm::Handle<std::vector<float> > mh_genPartPt;
      edm::Handle<std::vector<float> > mh_genPartEta;
      edm::Handle<std::vector<float> > mh_genPartPhi;
      edm::Handle<std::vector<float> > mh_genPartE;
      edm::Handle<std::vector<float> > mh_genPartID;
      edm::Handle<std::vector<float> > mh_genPartStatus;
      edm::Handle<std::vector<float> > mh_genPartMomID;
      edm::Handle<std::vector<float> > mh_genPartMom0ID;
      edm::Handle<std::vector<float> > mh_genPartMom1ID;
      edm::Handle<std::vector<float> > mh_genPartDau0ID;
      edm::Handle<std::vector<float> > mh_genPartDau1ID;
      
      edm::Handle<unsigned> mh_ngoodAK4Jets;
      edm::Handle<unsigned> mh_ngoodAK8Jets;
      edm::Handle<unsigned> mh_nlooseBTaggedAK4Jets;
      edm::Handle<unsigned> mh_nmediumBTaggedAK4Jets;
      edm::Handle<unsigned> mh_ntightBTaggedAK4Jets;
      edm::Handle<vector<unsigned> > mh_bjetsIdx;
      edm::Handle<vector<unsigned> > mh_wjetsIdx;
      edm::Handle<unsigned> mh_nWJets;
      edm::Handle<unsigned> mh_nHJets;
      edm::Handle<unsigned> mh_nTJets;

      edm::Handle<std::vector<unsigned> > mh_ak4UnmatchedIdx;
      edm::Handle<unsigned> mh_nAk4Unmatched;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx_lsubj;
      edm::Handle<std::vector<unsigned> > mh_hjetsIdx_lsubj;

      edm::Handle<double> mh_maxetaak4;
      edm::Handle<double> mh_MassLeading2AK8;
      edm::Handle<double> mh_DeltaEtaLeading2AK8;
      edm::Handle<double> mh_pt1stAK8;
      edm::Handle<double> mh_pt2ndAK8;
      edm::Handle<double> mh_mass1stAK8;
      edm::Handle<double> mh_mass2ndAK8;

      edm::Handle<vector<string> > h_trigName             ; iEvent.getByLabel (l_trigName               , h_trigName             );
      edm::Handle<float>  h_trigBit              ; iEvent.getByLabel (l_trigBit                , h_trigBit              );

      edm::Handle<vector<double> > mh_EvtWeight;


      iEvent.getByLabel("eventInfo", "evtInfoEventNumber", mh_evtNum);

      iEvent.getByLabel("electrons", "elPt", mh_elPt);
      iEvent.getByLabel("electrons", "elEta", mh_elEta);
      iEvent.getByLabel("electrons", "elPhi", mh_elPhi);
      iEvent.getByLabel("electrons", "elE", mh_elE);
      iEvent.getByLabel("electrons", "elCharge", mh_elCharge);
      iEvent.getByLabel("electrons", "elPt", mh_elisMedium);

      iEvent.getByLabel("muons", "muPt", mh_muPt);
      iEvent.getByLabel("muons", "muEta", mh_muEta);
      iEvent.getByLabel("muons", "muPhi", mh_muPhi);
      iEvent.getByLabel("muons", "muE", mh_muE);
      iEvent.getByLabel("muons", "muCharge", mh_muCharge);
      iEvent.getByLabel("muons", "muPt", mh_muIsTightMuon);
      
      iEvent.getByLabel("jetsAK4", "jetAK4Pt", mh_jetAK4Pt);
      iEvent.getByLabel("jetsAK4", "jetAK4GenPartonPt", mh_jetAK4GenPartonPt);
      iEvent.getByLabel("jetsAK4", "jetAK4Eta", mh_jetAK4Eta);
      iEvent.getByLabel("jetsAK4", "jetAK4GenPartonY", mh_jetAK4GenPartonY);
      iEvent.getByLabel("jetsAK4", "jetAK4Phi", mh_jetAK4Phi);
      iEvent.getByLabel("jetsAK4", "jetAK4E", mh_jetAK4E);
      iEvent.getByLabel("jetsAK4", "jetAK4HadronFlavour", mh_jetAK4HadronFlavour);
      iEvent.getByLabel("jetsAK4", "jetAK4CSV", mh_jetAK4CSV);
      iEvent.getByLabel("jetsAK4", "jetAK4Mass", mh_jetAK4Mass);	

      iEvent.getByLabel("anavars", "ak4UnmatchedIdx",mh_ak4UnmatchedIdx);
      iEvent.getByLabel("anavars", "nAk4Unmatched",mh_nAk4Unmatched);
      iEvent.getByLabel("anavars", "tjetsIdx-lsubj",mh_tjetsIdx_lsubj);
      iEvent.getByLabel("anavars", "hjetsIdx-lsubj",mh_hjetsIdx_lsubj);
      iEvent.getByLabel("anavars", "wjetsIdx",mh_wjetsIdx);
      

      iEvent.getByLabel("presel", "ak4goodjets", mh_jetAK4Good);
      iEvent.getByLabel("presel", "htak4jets", mh_htak4jets);
      iEvent.getByLabel("presel", "htak8jets", mh_htak8jets);
      iEvent.getByLabel("presel", "htak4trigjets", mh_htak4trigjets);

      iEvent.getByLabel("presel","bjetIdxs", mh_bjetsIdx);
      iEvent.getByLabel("presel","ngoodAK4Jets", mh_ngoodAK4Jets);
      iEvent.getByLabel("presel","ngoodAK8Jets", mh_ngoodAK8Jets);
      iEvent.getByLabel("presel","nbtaggedlooseAK4", mh_nlooseBTaggedAK4Jets);
      iEvent.getByLabel("presel","nbtaggedmediumAK4", mh_nmediumBTaggedAK4Jets);
      iEvent.getByLabel("presel","nbtaggedtightAK4", mh_ntightBTaggedAK4Jets);
      iEvent.getByLabel("presel","nWJets",mh_nWJets);
      iEvent.getByLabel("presel","nHJets",mh_nHJets);
      iEvent.getByLabel("presel","nTJets",mh_nTJets);
      iEvent.getByLabel("presel","maxetaak4", mh_maxetaak4);
      iEvent.getByLabel("presel","MassLeading2AK8", mh_MassLeading2AK8);
      iEvent.getByLabel("presel","DeltaEtaLeading2AK8",mh_DeltaEtaLeading2AK8);
      iEvent.getByLabel("presel","pt1stAK8",mh_pt1stAK8);
      iEvent.getByLabel("presel","pt2ndAK8",mh_pt2ndAK8);
      iEvent.getByLabel("presel","mass1stAK8",mh_mass1stAK8);
      iEvent.getByLabel("presel","mass2ndAK8",mh_mass2ndAK8);

      if(!_isData)
      	iEvent.getByLabel("presel","EvtWeight",mh_EvtWeight);

      iEvent.getByLabel("jetsAK8", "jetAK8Pt", mh_jetAK8Pt);
      iEvent.getByLabel("jetsAK8", "jetAK8Eta", mh_jetAK8Eta);
      iEvent.getByLabel("jetsAK8", "jetAK8Phi", mh_jetAK8Phi);
      iEvent.getByLabel("jetsAK8", "jetAK8E", mh_jetAK8E);
      iEvent.getByLabel("jetsAK8", "jetAK8Mass", mh_jetAK8Mass);
      iEvent.getByLabel("jetsAK8", "jetAK8vSubjetIndex0", mh_jetAK8subjetIndex0);
      iEvent.getByLabel("jetsAK8", "jetAK8vSubjetIndex1", mh_jetAK8subjetIndex1);
      iEvent.getByLabel("jetsAK8", "jetAK8HadronFlavour", mh_jetAK8HadronFlavour);
      iEvent.getByLabel("jetsAK8", "jetAK8nSubJets", mh_jetAK8nSubjets );
      
      iEvent.getByLabel("jetsAK8", "jetAK8filteredMass"    , mh_jetAK8FilteredMass   );
      iEvent.getByLabel("jetsAK8", "jetAK8trimmedMass"    , mh_jetAK8TrimmedMass   );
      iEvent.getByLabel("jetsAK8", "jetAK8prunedMass"    , mh_jetAK8PrunedMass   );
      iEvent.getByLabel("jetsAK8", "jetAK8softDropMass"    , mh_jetAK8SoftDropMass   );

      iEvent.getByLabel("jetsAK8", "jetAK8tau1", mh_jetAK8tau1);
      iEvent.getByLabel("jetsAK8", "jetAK8tau2", mh_jetAK8tau2);
      iEvent.getByLabel("jetsAK8", "jetAK8tau3", mh_jetAK8tau3);
      iEvent.getByLabel("presel", "ak8goodjets", mh_jetAK8Good);
      iEvent.getByLabel("presel", "htak8jets", mh_htak8jets);

      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagPt", mh_jetsCmsTopTagPt);
      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagEta", mh_jetsCmsTopTagEta);
      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagPhi", mh_jetsCmsTopTagPhi);
      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagE", mh_jetsCmsTopTagE);
      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagMass", mh_jetsCmsTopTagMass);
      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagsubjetIndex0", mh_jetsCmsTopTagsubjetIndex0);
      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagsubjetIndex1", mh_jetsCmsTopTagsubjetIndex1);
      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagHadronFlavour", mh_jetsCmsTopTagHadronFlavour);
      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagtau1", mh_jetsCmsTopTagtau1);
      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagtau2", mh_jetsCmsTopTagtau2);
      iEvent.getByLabel("jetsCmsTopTag", "jetsCmsTopTagtau3", mh_jetsCmsTopTagtau3);

      iEvent.getByLabel("subjetsAK8", "subjetAK8CSV", mh_subjetAK8CSVV1);

//      iEvent.getByLabel("analyze","HbbCandidates", mh_hbbCandidates);
/*
      iEvent.getByLabel("genPart", "genPartPt", mh_genPartPt);
      iEvent.getByLabel("genPart", "genPartEta", mh_genPartEta);
      iEvent.getByLabel("genPart", "genPartPhi", mh_genPartPhi);
      iEvent.getByLabel("genPart", "genPartE", mh_genPartE);
      iEvent.getByLabel("genPart", "genPartID", mh_genPartID);
      iEvent.getByLabel("genPart", "genPartStatus", mh_genPartStatus);
      //iEvent.getByLabel("genPart", "genPartMomID", mh_genPartMomID);
      iEvent.getByLabel("genPart", "genPartMom0ID", mh_genPartMom0ID);
      iEvent.getByLabel("genPart", "genPartMom1ID", mh_genPartMom1ID);
      iEvent.getByLabel("genPart", "genPartDau0ID", mh_genPartDau0ID);
      iEvent.getByLabel("genPart", "genPartDau1ID", mh_genPartDau1ID);
*/
//      const std::vector<float> * jetcsv = mh_jetAK4CSV.product();
      const std::vector<float> * jetpt = mh_jetAK4Pt.product();
      const std::vector<float> * jeteta = mh_jetAK4Eta.product();
      const std::vector<float> * jetphi = mh_jetAK4Phi.product();
      const std::vector<float> * jetM = mh_jetAK4Mass.product();
      const std::vector<float> * jetflavor = mh_jetAK4HadronFlavour.product();
   //   const std::vector<unsigned> * jetgood = mh_jetAK4Good.product();
      const std::vector<float> * jetCSV = mh_jetAK4CSV.product();
      const std::vector<unsigned> * ak4UnmatchedIdx = mh_ak4UnmatchedIdx.product();

      const std::vector<float> * jet8pt = mh_jetAK8Pt.product();
      const std::vector<float> * jet8eta = mh_jetAK8Eta.product();
      const std::vector<float> * jet8phi = mh_jetAK8Phi.product();
      const std::vector<float> * jet8M = mh_jetAK8Mass.product();
      const std::vector<float> * jet8nSubjets = mh_jetAK8nSubjets.product();
      const std::vector<unsigned> * jet8good = mh_jetAK8Good.product();
      const std::vector<float> * softDropMassAK8 = mh_jetAK8SoftDropMass.product();
      const std::vector<float> * trimmedMassAK8 = mh_jetAK8TrimmedMass.product();
      const std::vector<float> * jetAK8subjetIndex0 = mh_jetAK8subjetIndex0.product();
      const std::vector<float> * jetAK8subjetIndex1 = mh_jetAK8subjetIndex1.product();

      const unsigned * nAK4Unmatched = mh_nAk4Unmatched.product();
      const std::vector<unsigned> * tjetsIdx_lsubj = mh_tjetsIdx_lsubj.product();
      const std::vector<unsigned> * hjetsIdx_lsubj = mh_hjetsIdx_lsubj.product();
      const std::vector<unsigned> * wjetsIdx = mh_wjetsIdx.product();

      const std::vector<unsigned> * bjetsIdx = mh_bjetsIdx.product();

//      const std::vector<float> * jetAK8nSubjets = mh_jetAK8nSubjets.product();

      const std::vector<float> * subjet8CSV = mh_subjetAK8CSVV1.product();
/*
      const std::vector<float> * genPartID = mh_genPartID.product();
      const std::vector<float> * genPartMomID = mh_genPartMom0ID.product();
      const std::vector<float> * genPartStatus= mh_genPartStatus.product();
      const std::vector<float> * genPartEta = mh_genPartEta.product();
      const std::vector<float> * genPartPhi = mh_genPartPhi.product();
*/
      const double * htak4jets = mh_htak4jets.product();
      htak4 = *htak4jets;

      const double * htak4trigjets = mh_htak4trigjets.product();
      const double * htak8jets = mh_htak8jets.product();


      const unsigned * ngoodAK4Jets = mh_ngoodAK4Jets.product();
      const unsigned * ngoodAK8Jets = mh_ngoodAK8Jets.product();
//      const unsigned * nlooseBTaggedAK4Jets = mh_nlooseBTaggedAK4Jets.product();
//      const unsigned * nmediumBTaggedAK4Jets = mh_nmediumBTaggedAK4Jets.product();
//      const unsigned * ntightBTaggedAK4Jets = mh_ntightBTaggedAK4Jets.product();
      const unsigned * nWJets = mh_nWJets.product();
      const unsigned * nHJets = mh_nHJets.product();
      const unsigned * nTJets = mh_nTJets.product();
      const double * maxetaak4 = mh_maxetaak4.product();
      const double * MassLeading2AK8 = mh_MassLeading2AK8.product();
      const double * DeltaEtaLeading2AK8 = mh_DeltaEtaLeading2AK8.product();
      const double * pt1stAK8 = mh_pt1stAK8.product();
      const double * pt2ndAK8 = mh_pt2ndAK8.product();
      const double * mass1stAK8 = mh_mass1stAK8.product();
      const double * mass2ndAK8 = mh_mass2ndAK8.product();
//      const double * hbbCands = mh_hbbCandidates.product();

  //    const std::vector<float> * jetAK8Phi = mh_jetAK8Phi.product();
  //    const std::vector<float> * jetAK8Eta = mh_jetAK8Eta.product();
  //    const std::vector<float> * jetAK8Mass = mh_jetAK8Mass.product();

//      const ULong64_t * evtNum = mh_evtNum.product();

      const std::vector<double> * EvtWeight_;

      if(!_isData) EvtWeight_ = mh_EvtWeight.product();
	else {
		EvtWeight_ = new std::vector<double>{1};
	}
			
//	Trigger
//
// if(_isData){
  //unsigned int hltdecisions(0) ;

  bTrigger->clear();
  for ( unsigned int i = 0 ; i < h_trigName.product()->size() ; i++ ) {

        //Support regex pattern matching: wildcards . and .*
        //
       // cout << hltPaths_.size()<<endl;
       for( unsigned int j = 0; j < hltPaths_.size() ; j++ ) {

           string hltname = h_trigName.product()->at(i);
           boost::regex pattern(hltPaths_[j]);

           bTrigger->push_back(boost::regex_match(hltname , pattern)>0);
          // cout << hltname << "  " << hltPaths_[j] << "  " << (*bTrigger)[j] << endl;


           //hltdecisions += (pow(2,i) && bPass);
       }
   }

   // Setup cut conditions.	

// }
// else {
//	if (*htak4trigjets < 800) return;
	
 //}
      //cout << "conditions"<<endl;
      

	nAK8 = (*ngoodAK8Jets);

//	cout << "hjetsIdx_lsubj: " << hjetsIdx_lsubj->size() << endl; 
//	cout << "tjetsIdx_lsubj: " << tjetsIdx_lsubj->size() << endl; 
	
	subjAK8->clear();
	idxHTag->clear();
	idxTTag->clear();
	ptAK8->clear();
	etaAK8->clear();
	EvtWeight->clear();
	AK8Idx->clear();
	idxbTag->clear();

	for (unsigned i = 0 ; i < *ngoodAK8Jets ; i++) {
	    ptAK8->push_back((*jet8pt)[(*jet8good)[i]]);
	    etaAK8->push_back((*jet8eta)[(*jet8good)[i]]);
	    AK8Idx->push_back((*jet8good)[i]);
//	    subjAK8->push_back((*jet8nSubjets)[
	    
	}

	idxHTag->reserve(hjetsIdx_lsubj->size());
	idxTTag->reserve(tjetsIdx_lsubj->size());
	idxWTag->reserve(wjetsIdx->size());
	EvtWeight->reserve(EvtWeight_->size());
	idxbTag->reserve(bjetsIdx->size());

	std::copy(hjetsIdx_lsubj->begin(), hjetsIdx_lsubj->end(),
              std::back_inserter(*idxHTag));

	std::copy(tjetsIdx_lsubj->begin(), tjetsIdx_lsubj->end(),
              std::back_inserter(*idxTTag));

        std::copy(wjetsIdx->begin(), wjetsIdx->end(),
              std::back_inserter(*idxWTag));

        std::copy(EvtWeight_->begin(), EvtWeight_->end(),
              std::back_inserter(*EvtWeight));

        std::copy(bjetsIdx->begin(), bjetsIdx->end(),
              std::back_inserter(*idxbTag));


//	cout << "nAk8: " <<nAK8 << endl;
/*
	for(unsigned i = 0 ; i < idxTTag->size() ; i++) {
	   
	    cout << "TTag_lsubj " <<i << ": " << (*tjetsIdx_lsubj)[i] << endl;
	}
	for(unsigned i = 0 ; i < idxTTag->size() ; i++) {
	   
	    cout << "TTag " <<i << ": " << (*idxTTag)[i] << endl;
	}
	for(unsigned i = 0 ; i < idxHTag->size() ; i++) {
	   
	    cout << "HTag " <<i << ": " << (*idxHTag)[i] << endl;
	}
*/
	//idxTTag = &((*tjetsIdx_lsubj)[0]);
	//idxHTag = &((*hjetsIdx_lsubj)[0]);


        bx2AK8Jets = (*ngoodAK8Jets == 2);


        // 2 AK8 Jets
        b2AK8Jets = (*ngoodAK8Jets > 1);
        //
        // 6+ AK4 Jets
        b6AK4Jets = (*ngoodAK4Jets > 5 );
        b2AK4Jets = (*nAK4Unmatched > 1 );
        b1AK4Jets = (*nAK4Unmatched > 0 );
        
        // TMass        
        bTMass = (( *mass1stAK8 > 160 && *mass1stAK8 < 190) || (*mass2ndAK8 > 160 && *mass2ndAK8 < 190));
       
        
        //HMass
        bHMass = (( *mass1stAK8 > 110 && *mass1stAK8 < 140) || (*mass2ndAK8 > 110 && *mass2ndAK8 < 140));
        
        // H Tag
        bHTag = (hjetsIdx_lsubj->size() > 0);

//	cout << "tags "<< tjetsIdx_lsubj->size()<<endl;
//	cout << "subjets "<< jet8nSubjets->size()<<":"<<subjet8CSV->size()<<endl;
        
        // T Tag
        bTTag = (tjetsIdx_lsubj->size() > 0);
//	cout << "------------------------" <<endl;	
//	cout << "Total subjets: " << subjet8CSV->size() << endl;
	if(subjet8CSV->size() > 0){
		bool bTTagSubj1 = false;
		bool bTTagSubj2 = false;
		unsigned subjIdx = 0;

		for (unsigned i = 0 ; i < jet8nSubjets->size() ; i++) {
		   // cout << "Jet " << i << "  subjets: " << (*jet8nSubjets)[i] << endl;
		    unsigned nbSub = 0;
		    for(unsigned k = 0 ; k < hjetsIdx_lsubj->size() ; k++) 
		      if(i == (*hjetsIdx_lsubj)[k])
///		          cout << "H Jet: "<< i << endl; //<< ": "<< (*jet8nSubjets)[i] <<" subjets" << endl; 
//			cout << "subjet idx0: " << (*jetAK8subjetIndex0)[i] << endl;
///			cout << "subjet idx1: " << (*jetAK8subjetIndex1)[i] << endl;
//			cout << "CSV0: " << (*subjet8CSV)[(*jetAK8subjetIndex0)[i]] << endl;
//			cout << "CSV1: " << (*subjet8CSV)[(*jetAK8subjetIndex1)[i]]	<< endl;
			if((*jetAK8subjetIndex0)[i]!=-1 and (*subjet8CSV)[(*jetAK8subjetIndex0)[i]]>.605) nbSub++; 
			if((*jetAK8subjetIndex1)[i]!=-1 and (*subjet8CSV)[(*jetAK8subjetIndex1)[i]]>.605) nbSub++; 
/*
		    for (unsigned j = 0 ; j < (*jet8nSubjets)[i] ; j++ ) {
			cout << "subjet: " << subjIdx+j<<" = " << (*subjet8CSV)[subjIdx+j] <<endl;
			if((*subjet8CSV)[subjIdx+j]>.605) {
			    nbSub++;
			}			
		    }
*/
		    subjAK8->push_back(nbSub);
		    subjIdx += (*jet8nSubjets)[i];
		
		}		


		unsigned subj1Idx = 0;
		unsigned subj2Idx = 0;
		if(tjetsIdx_lsubj->size() > 0) {
		   for (unsigned i = 0 ; i < (*tjetsIdx_lsubj)[0] ; i++) {
//			cout <<"t idx[0] " << (*tjetsIdx_lsubj)[0] << endl;
			subj1Idx += (*jet8nSubjets)[i];
		   }
//		   cout << "subj1Idx: " <<  subj1Idx << endl; 
		   bTTagSubj1 = ((*subjet8CSV)[subj1Idx]>.605);
		}
		if(tjetsIdx_lsubj->size() > 1) {
		    for (unsigned i = 0 ; i < (*tjetsIdx_lsubj)[1] ; i++) {
//			cout <<"t idx[1] " << (*tjetsIdx_lsubj)[1] << endl;
			subj2Idx += (*jet8nSubjets)[i];
		    }
//		    cout << "subj2Idx: " <<  subj2Idx << endl; 
		    bTTagSubj2 = ((*subjet8CSV)[subj2Idx]>.605);
		}
		
		

		bTTagSubj = bTTagSubj1 or bTTagSubj2;
	}
        //
//        cout << "H T Tag" << endl;
        //                                                                                                 // b-tagged jets
        //
        //unsigned looseBTag, mediumBTag, tightBTag;
        looseBTag = mediumBTag = tightBTag = 0;
        //
        for( unsigned ak4idx : *ak4UnmatchedIdx) {
                                        if(bjetsIdx->end() != std::find(bjetsIdx->begin(), bjetsIdx->end(), ak4idx)) {
                           if((*jetCSV)[ak4idx] > .97) { tightBTag++;}
                           if((*jetCSV)[ak4idx] > .89) { mediumBTag++;}
                           if((*jetCSV)[ak4idx] > .605) { looseBTag++;}
                                                                                                       }
        }
        TLorentzVector J1, J2;
	//float relM = 0;

        if(jet8good->size() >= 2) {
                J1.SetPtEtaPhiM((*jet8pt)[(*jet8good)[0]],
                         (*jet8eta)[(*jet8good)[0]],
                         (*jet8phi)[(*jet8good)[0]],
                         (*jet8M)[(*jet8good)[0]]);

                J2.SetPtEtaPhiM((*jet8pt)[(*jet8good)[1]],
                         (*jet8eta)[(*jet8good)[1]],
                         (*jet8phi)[(*jet8good)[1]],
                         (*jet8M)[(*jet8good)[1]]);

                relM = ((*jet8M)[(*jet8good)[0]] + (*jet8M)[(*jet8good)[1]]) / (J1 + J2).M();

        }
        //
        bLoose1 = (looseBTag > 0);
//        bool bLoose2 = (looseBTag > 1);

        bMedium1 = (mediumBTag > 0);
        //      bool bMedium2 = (mediumBTag > 1);

        bTight1 = (tightBTag > 0);
        //      bool bTight2 = (tightBTag > 1);

        softDropMassLeadAK8 = (*softDropMassAK8)[(*jet8good)[0]];
        trimmedMassLeadAK8 = (*trimmedMassAK8)[(*jet8good)[0]];

	//Mass of T' candidate
	
//	cout << "Tprime" << endl;
	if(jet8good->size() >= 2 && idxHTag->size() >0 && idxTTag->size() > 0) {
 		TLorentzVector TCand, HCand;
		
		HCand.SetPtEtaPhiM((*jet8pt)[(*idxHTag)[0]],
                         (*jet8eta)[(*idxHTag)[0]],
                         (*jet8phi)[(*idxHTag)[0]],
                         (*jet8M)[(*idxHTag)[0]]);

                TCand.SetPtEtaPhiM((*jet8pt)[(*idxTTag)[0]],
                         (*jet8eta)[(*idxTTag)[0]],
                         (*jet8phi)[(*idxTTag)[0]],
                         (*jet8M)[(*idxTTag)[0]]);

		massTprime = (HCand + TCand).M();
	}
//	cout << "Tprime" << endl;

     //   ptLeadingAK4=pt2ndAK4=pt3rdAK4=pt4thAK4=pt5thAK4=pt6thAK4 = 0;
//	etaLeadingAK4=eta2ndAK4=eta3rdAK4=eta4thAK4=eta5thAK4=eta6thAK4 = 0;

        if(ak4UnmatchedIdx->size() >0 ){
                ptLeadingAK4 = (*jetpt)[(*ak4UnmatchedIdx)[0]];
                histos["ptLeadingAK4"]->Fill(ptLeadingAK4);
		etaLeadingAK4 = (*jeteta)[(*ak4UnmatchedIdx)[0]];
                histos["etaLeadingAK4"]->Fill(etaLeadingAK4);
        }

        if(ak4UnmatchedIdx->size() >1 ){
                pt2ndAK4 = (*jetpt)[(*ak4UnmatchedIdx)[1]];
                histos["pt2ndAK4"]->Fill(pt2ndAK4);
		etaLeadingAK4 = (*jeteta)[(*ak4UnmatchedIdx)[1]];
                histos["eta2ndAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[1]]);
        }
        if(ak4UnmatchedIdx->size() >2 ){
                pt3rdAK4 = (*jetpt)[(*ak4UnmatchedIdx)[2]];
                histos["pt3rdAK4"]->Fill(pt3rdAK4);
		etaLeadingAK4 = (*jeteta)[(*ak4UnmatchedIdx)[2]];
                histos["eta3rdAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[2]]);
        }
        if(ak4UnmatchedIdx->size() >3 ){
                pt4thAK4 = (*jetpt)[(*ak4UnmatchedIdx)[3]];
                histos["pt4thAK4"]->Fill(pt4thAK4);
		etaLeadingAK4 = (*jeteta)[(*ak4UnmatchedIdx)[3]];
                histos["eta4thAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[3]]);
        }
        if(ak4UnmatchedIdx->size() > 4 ){
                pt5thAK4 = (*jetpt)[(*ak4UnmatchedIdx)[4]];
                histos["pt5thAK4"]->Fill(pt5thAK4);
		etaLeadingAK4 = (*jeteta)[(*ak4UnmatchedIdx)[4]];
                histos["eta5thAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[4]]);
        }
        if(ak4UnmatchedIdx->size() >5 ){
                pt6thAK4 = (*jetpt)[(*ak4UnmatchedIdx)[5]];
                histos["pt6thAK4"]->Fill(pt6thAK4);
		etaLeadingAK4 = (*jeteta)[(*ak4UnmatchedIdx)[5]];
                histos["eta6thAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[5]]);
        }
	//cout << "Ak4" <<endl;
        bAK4LeadingPt = (ptLeadingAK4 < 200 );
        bMass2AK8_1200 = ( *MassLeading2AK8 > 950 and *MassLeading2AK8 < 1400  );
        bMass2AK8_1700 = ( *MassLeading2AK8 >1400 and *MassLeading2AK8 < 1900  );
        bSoftDropMassAK8 = (softDropMassLeadAK8 > 60);
        bTrimmedMassAK8 = ( trimmedMassLeadAK8 > 60);

        brelM = (relM > 0.15 && relM < 0.35);
        // Rel Pt
        relpt = (*pt1stAK8 + *pt2ndAK8) / *htak4jets;
        brelpt = (relpt > 0.65);


        bForwardJet = false;

	    fMaxEtaAK4 = 0;
            for( unsigned int i = 0 ; i < ak4UnmatchedIdx->size() ; i++ )
            {

                if(jeteta){
			//cout << jeteta <<"  " << i << endl;
                  if( fabs((*jeteta)[(*ak4UnmatchedIdx)[i]]) > 1.5 )
                        bForwardJet = true;
		  if( fabs((*jeteta)[(*ak4UnmatchedIdx)[i]]) > fMaxEtaAK4)
			fMaxEtaAK4 = fabs((*jeteta)[(*ak4UnmatchedIdx)[i]]);
		}
           }

  histos[ "HT_presel" ]->Fill(*htak4jets);
  histos[ "pt1stAK8_presel" ]->Fill( *pt1stAK8);
  histos[ "eta1stAK8_presel" ]->Fill ((*jet8eta)[(*jet8good)[0]]);

  if(bx2AK8Jets) {
  	histos[ "pt2ndAK8_presel" ]->Fill (*pt2ndAK8);
  	histos[ "eta2ndAK8_presel" ]->Fill ((*jet8eta)[(*jet8good)[1]]); 
  }

  histos["ptLeadingAK4_presel"]->Fill(ptLeadingAK4); 
  histos["etaLeadingAK4_presel"]->Fill(etaLeadingAK4); 
  histos["pt2ndAK4_presel"]->Fill(pt2ndAK4); 
  histos["eta2ndAK4_presel"]->Fill(eta2ndAK4); 
  histos[ "maxetaAK4_presel" ]->Fill(fMaxEtaAK4);


  histos [ "BtagsAK4_t_presel" ] -> Fill(tightBTag);
  histos [ "relM_presel" ] -> Fill(relM);

  if( bx2AK8Jets ){
  	histos [ "TprimeMass_presel" ]->Fill(*MassLeading2AK8);
  }
  histos [ "softDropMass_presel" ] -> Fill(softDropMassLeadAK8);

  if( bx2AK8Jets && bHTag && bTTag && brelM && bSoftDropMassAK8 && bMass2AK8_1200)
  	histos [ "BtagsAK4_t_sel" ] -> Fill(tightBTag);

  if( bx2AK8Jets && bHTag && bTTag  && bSoftDropMassAK8 && bMass2AK8_1200 && bTight1 )
  	histos [ "relM_sel" ] -> Fill(relM);

  if( bx2AK8Jets && bHTag && bTTag  && bSoftDropMassAK8 && brelM && bTight1 )
	  histos [ "TprimeMass_sel" ]->Fill(*MassLeading2AK8); 

  if( bx2AK8Jets && bHTag && bTTag && brelM && bTight1 && bMass2AK8_1200) 
  	histos [ "softDropMass_sel" ] -> Fill(softDropMassLeadAK8);

  if( bx2AK8Jets && bHTag && bTTag && brelM && bTight1 && bMass2AK8_1200 && bSoftDropMassAK8)
  	histos[ "maxetaAK4_sel" ]->Fill(fMaxEtaAK4);

//	if(!(b2AK8Jets && bTight1 && bHTag && bTTag && brelM && bSoftDropMassAK8 && bMass2AK8_1700)) return;

        // dPhi 2 AK8
        
        bool bdPhiAK8 = false;
                   if(jet8good->size() > 1) {
        
                        float dPhiLeadingAK8 = deltaPhi((*jet8phi)[(*jet8good)[0]],(*jet8phi)[(*jet8good)[1]]);
                        histos["dPhiLeadingAK8"]->Fill (dPhiLeadingAK8);
                        bdPhiAK8 = ( dPhiLeadingAK8 > 2);
        
                        histos["eta1stAK8"]->Fill( (*jet8eta)[(*jet8good)[0]]);
                        histos["eta2ndAK8"]->Fill( (*jet8eta)[(*jet8good)[1]]);
                   }
        // Rel pt
        
        //
    //  if(*nAk4Unmatched < 4) return;

      int idx1 = -1;
      int idx2 = -1; 


//      int iBTags = 0;

//     cout << "Evt: " << evtNum << endl;
	//cout << "histos1" << endl;	



	histos["AK4Ht"]->Fill(*htak4jets);
	histos["AK4Ht_reweight"]->Fill(*htak4jets,(*EvtWeight_)[0]);
	histos["AK8Ht"]->Fill(*htak8jets);
	histos["AK4trigHt"]->Fill(*htak4trigjets);

	histos["nTTags"]->Fill(*nTJets);
	histos["nWTags"]->Fill(*nWJets);
	histos["nHTags"]->Fill(*nHJets);

	histos["nTTags_lsubj"]->Fill(tjetsIdx_lsubj->size());
	histos["nHTags_lsubj"]->Fill(hjetsIdx_lsubj->size());

	histos["AK4Jets"]->Fill(ak4UnmatchedIdx->size());

	histos["ngoodAK4Jets"]->Fill(*ngoodAK4Jets);
        histos["ngoodAK8Jets"]->Fill(*ngoodAK8Jets);
	histos["ngoodAK4Jets_Unm"]->Fill(*nAK4Unmatched);



        histos["nWJets"]->Fill(*nWJets);
        histos["nHJets"]->Fill(*nHJets);
        histos["maxetaak4"]->Fill(*maxetaak4);
        histos["MassLeading2AK8"]->Fill(*MassLeading2AK8);
        histos["DeltaEtaLeading2AK8"]->Fill(*DeltaEtaLeading2AK8);
        histos["pt1stAK8"]->Fill(*pt1stAK8);
        histos["pt2ndAK8"]->Fill(*pt2ndAK8);
        histos["mass1stAK8"]->Fill(*mass1stAK8);
        histos["mass2ndAK8"]->Fill(*mass2ndAK8);


        histos[ "relM" ]->Fill(relM);


 	//cout << "Jet Pair" << endl;
	// Determine Mass of closest JetPair.
	if(idx1 > -1) 
	{
		TLorentzVector j1,j2;

		j1.SetPtEtaPhiM((*jetpt)[idx1],(*jeteta)[idx1],(*jetphi)[idx1],(*jetM)[idx1]);
		j2.SetPtEtaPhiM((*jetpt)[idx2],(*jeteta)[idx2],(*jetphi)[idx2],(*jetM)[idx2]);
	
		histos["AK4JetPairMass"]->Fill((j1+j2).M());	
		histos["AK4JetFlavor"]->Fill((*jetflavor)[idx1]);
		histos["AK4JetFlavor"]->Fill((*jetflavor)[idx2]);
	}
	
/*	
	if( *evtNum < 10) {
		for(unsigned int i = 0 ; i < genPartID->size(); i++)
		{
		   if(abs((*genPartID)[i]) == 5 || abs((*genPartID)[i]) == 25 || abs((*genPartID)[i]) == 6)
			std::cout << i << ":  " << (*genPartID)[i] << "      " << (*genPartMomID)[i] << "       " << (*genPartStatus)[i] << " Eta: " << (*genPartEta)[i]  << " Phi: " << (*genPartPhi)[i] << std::endl;

		}
		for(unsigned int i = 0; i < jetAK8Eta->size() ; i++)
			{
			    std::cout << "AK8 Jet: " << "#" << i << "  Eta: " << (*jetAK8Eta)[i] << "  Phi: " << (*jetAK8Phi)[i] << "  Mass: " << (*jetAK8Mass)[i] << std::endl; 
		}
	}
*/


	histos["AK4BTags-l"]->Fill(looseBTag);
	histos["AK4BTags-m"]->Fill(mediumBTag);
	histos["AK4BTags-t"]->Fill(tightBTag);

	//cout << "BTag " <<endl; 

	
/*
	double mass2AK4 = 0;

        if(jetgood->size() >= 2) {
                J1.SetPtEtaPhiM((*jetpt)[(*jetgood)[0]],
                         (*jeteta)[(*jetgood)[0]],
                         (*jetphi)[(*jetgood)[0]],
                         (*jetM)[(*jetgood)[0]]);

                J2.SetPtEtaPhiM((*jetpt)[(*jetgood)[1]],
                         (*jeteta)[(*jetgood)[1]],
                         (*jetphi)[(*jetgood)[1]],
                         (*jetM)[(*jetgood)[1]]);

                mass2AK4 =  (J1 + J2).M();
	
 	}
*/
	//cout << "Relm" <<endl;



	if(ak4UnmatchedIdx->size() >0 ){
		histos["ptLeadingAK4"]->Fill(ptLeadingAK4);
		histos["etaLeadingAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[0]]);
	}

	if(ak4UnmatchedIdx->size() >1 ){
		histos["pt2ndAK4"]->Fill(pt2ndAK4);
		histos["eta2ndAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[1]]);
	}
	if(ak4UnmatchedIdx->size() >2 ){
		histos["pt3rdAK4"]->Fill(pt3rdAK4);
		histos["eta3rdAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[2]]);
	}
	if(ak4UnmatchedIdx->size() >3 ){
		histos["pt4thAK4"]->Fill(pt4thAK4);
		histos["eta4thAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[3]]);
	}
	if(ak4UnmatchedIdx->size() > 4 ){
		histos["pt5thAK4"]->Fill(pt5thAK4);
		histos["eta5thAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[4]]);
	}
	if(ak4UnmatchedIdx->size() >5 ){
		histos["pt6thAK4"]->Fill(pt6thAK4);
		histos["eta6thAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[5]]);
	}


	//Histos
	//
	// Tagged AK8 as H Cand
	for ( unsigned hidx : *hjetsIdx_lsubj)
		histos["HTagCandidateMass"]->Fill((*jet8M)[hidx]); 
	for (unsigned hidx : *jet8good) {
		if ((*jet8nSubjets)[hidx] >1 and (*jet8nSubjets)[hidx] < 3 )
			histos["HCandidateMass"]->Fill((*jet8M)[hidx]);
	}

	//Htags vs TTags
	histos2["HvsT"]->Fill(hjetsIdx_lsubj->size(),tjetsIdx_lsubj->size());
	
	//Exactly two AK8 histos
	if ( bx2AK8Jets ) {
		for( unsigned idx : *ak4UnmatchedIdx) {
			 histos["2AK8_AK4CSV"]->Fill((*jetCSV)[idx]);
			 histos["2AK8_AK4pt"]->Fill((*jetpt)[idx]);
			 histos["2AK8_AK4eta"]->Fill((*jeteta)[idx]);
			 histos["2AK8_nAK4"]->Fill(ak4UnmatchedIdx->size());
		}
	}


	//


	//std::cout << " main Selection " << std::endl;

	//Main Selection
	//

	histos[ "Selection" ]->Fill(0) ; 
	if( b2AK8Jets )
		histos[ "Selection" ]->Fill(1) ; 
	if( b2AK8Jets && b2AK4Jets ) 
		histos[ "Selection" ]->Fill(2) ; 
	if( b2AK8Jets && bTTag) 
		histos[ "Selection" ]->Fill(3) ; 
	if( b2AK8Jets && bMedium1) 
		histos[ "Selection" ]->Fill(4) ; 
	if( b2AK8Jets && bHTag) 
		histos[ "Selection" ]->Fill(5) ; 
	if( b2AK8Jets && bForwardJet) 
		histos[ "Selection" ]->Fill(6) ; 
	if( b2AK8Jets && brelpt) 
		histos[ "Selection" ]->Fill(7) ; 
	if( b2AK8Jets && brelM) 
		histos[ "Selection" ]->Fill(8) ; 
	if( b2AK8Jets && bAK4LeadingPt) 
		histos[ "Selection" ]->Fill(9) ; 
	if( b2AK8Jets && bSoftDropMassAK8) 
		histos[ "Selection" ]->Fill(10) ; 
	if( b2AK8Jets && bTrimmedMassAK8) 
		histos[ "Selection" ]->Fill(11) ; 
	if( b2AK8Jets && bLoose1) 
		histos[ "Selection" ]->Fill(12) ; 
	if( b2AK8Jets && bTight1) 
		histos[ "Selection" ]->Fill(13) ; 
	if( b2AK8Jets && b1AK4Jets) 
		histos[ "Selection" ]->Fill(14) ; 
	if( b2AK8Jets && bdPhiAK8) 
		histos[ "Selection" ]->Fill(15) ; 
	if( b2AK8Jets && bMass2AK8_1200) 
		histos[ "Selection" ]->Fill(16) ; 
	if( b2AK8Jets && bMass2AK8_1700) 
		histos[ "Selection" ]->Fill(17) ; 
	if( b2AK8Jets && bTight1 && bHTag && bTTag && brelM && bSoftDropMassAK8 && bMass2AK8_1200) 
		histos[ "Selection" ]->Fill(18) ; 
	if( b2AK8Jets && bTight1 && bHTag && bTTag && brelM && bSoftDropMassAK8 && bMass2AK8_1700) 
		histos[ "Selection" ]->Fill(19) ; 
/*
        histos[ "Selection2" ]->Fill(0) ;
        if( b2AK8Jets && bHTag )
                histos[ "Selection2" ]->Fill(1) ;
        if( b2AK8Jets && b5AK4Jets && bHTag)
                histos[ "Selection2" ]->Fill(2) ;
        if(b2AK8Jets && b5AK4Jets && bLoose2 && bHTag)
                histos[ "Selection2" ]->Fill(3) ;
        if( b2AK8Jets && b5AK4Jets && bLoose2 && bTTag && bHTag)
                histos[ "Selection2" ]->Fill(4) ;
        if( b2AK8Jets && b5AK4Jets && bLoose3 && bHTag)
                histos[ "Selection2" ]->Fill(5) ;
        if( b2AK8Jets && b5AK4Jets && bLoose3 && bTTag && bHTag)
                histos[ "Selection2" ]->Fill(6) ;
        if( b2AK8Jets && b5AK4Jets && bLoose2 && bForwardJet && bHTag)
                histos[ "Selection2" ]->Fill(7) ;
        if( b2AK8Jets && b5AK4Jets && bLoose3 && bForwardJet && bHTag)
                histos[ "Selection2" ]->Fill(8) ;
        if( b2AK8Jets && b4AK4Jets && bLoose2 && bHTag)
                histos[ "Selection2" ]->Fill(9) ;
        if( b2AK8Jets && b4AK4Jets && bLoose2 && bForwardJet && bHTag)
                histos[ "Selection2" ]->Fill(10) ;
        if( b2AK8Jets && b4AK4Jets && bLoose2 && bTTag && bForwardJet && bHTag)
                histos[ "Selection2" ]->Fill(11) ;
        if( b2AK8Jets && b5AK4Jets && bLoose3 && bTTag && bForwardJet && bHTag)
                histos[ "Selection2" ]->Fill(12) ;
        if( b2AK8Jets && b5AK4Jets && bLoose3 && brelpt && brelM && bHTag)
                histos[ "Selection2" ]->Fill(13) ;
        if( b2AK8Jets && b5AK4Jets && bLoose3 && bForwardJet && brelpt && brelM && bHTag)
                histos[ "Selection2" ]->Fill(14) ;
        if( b4AK4Jets && brelpt && brelM && bHTag)
                histos[ "Selection2" ]->Fill(15) ;
        if( b4AK4Jets && bForwardJet && brelpt && brelM && bHTag)
                histos[ "Selection2" ]->Fill(16) ;
        if( b4AK4Jets && bLoose2 && brelpt && brelM && bHTag)
                histos[ "Selection2" ]->Fill(17) ;
        if( b4AK4Jets && bLoose2 && bForwardJet && brelpt && brelM && bHTag)
                histos[ "Selection2" ]->Fill(18) ;
        if( b2AK8Jets && b4AK4Jets && bForwardJet && brelpt && brelM && bHTag)
                histos[ "Selection2" ]->Fill(19) ;
        if( b2AK8Jets && b4AK4Jets && bLoose2 && brelpt && brelM && bHTag)
                histos[ "Selection2" ]->Fill(20) ;
        if( b2AK8Jets && b4AK4Jets && bLoose2 && bForwardJet && brelpt && brelM && bHTag)
                histos[ "Selection2" ]->Fill(21) ;

*/


	 if( bTTag && bHTag) {
                histos[ "SidebandD-M" ]->Fill(*MassLeading2AK8) ;
                histos[ "SidebandD-HT" ]->Fill(*htak4jets) ;
	 }
	 if( !bTTag && !bHTag) {
                histos[ "SidebandA-M" ]->Fill(*MassLeading2AK8) ;
                histos[ "SidebandA-HT" ]->Fill(*htak4jets) ;
	 }
	 if(  bTTag && !bHTag) {
                histos[ "SidebandC-M" ]->Fill(*MassLeading2AK8) ;
                histos[ "SidebandC-HT" ]->Fill(*htak4jets) ;
	 }
	 if( !bTTag && bHTag) {
                histos[ "SidebandB-M" ]->Fill(*MassLeading2AK8) ;
                histos[ "SidebandB-HT" ]->Fill(*htak4jets) ;
	 }

	cutTree->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void 
TprimeAna::beginJob()
{


//  cout << "begin job";
  cutTree = fs->make<TTree>("cutTree","cut variables");

  cutTree->Branch("softDropMassLeadAK8",&softDropMassLeadAK8,"softDropMassLeadAK8/D");
  cutTree->Branch("trimmedMassLeadAK8", &trimmedMassLeadAK8, "trimmedMassLeadAK8/D");
  cutTree->Branch("ptLeadingAK4", &ptLeadingAK4, "ptLeadingAK4/D");
  cutTree->Branch("etaLeadingAK4", &etaLeadingAK4, "etaLeadingAK4/D");
  cutTree->Branch("pt2ndAK4", &pt2ndAK4, "pt2ndAK4/D");
  cutTree->Branch("eta2ndAK4", &eta2ndAK4, "eta2ndAK4/D");
  cutTree->Branch("pt3rdAK4", &pt3rdAK4, "pt3rdAK4/D");
  cutTree->Branch("eta3rdAK4", &eta3rdAK4, "eta3rdAK4/D");
  cutTree->Branch("pt4thAK4", &pt4thAK4, "pt4thAK4/D");
  cutTree->Branch("eta4thAK4", &eta4thAK4, "eta4thAK4/D");
  cutTree->Branch("pt5thAK4", &pt5thAK4, "pt5thAK4/D");
  cutTree->Branch("eta5thAK4", &eta5thAK4, "eta5thAK4/D");
  cutTree->Branch("pt6thAK4", &pt6thAK4, "pt6thAK4/D");
  cutTree->Branch("eta6thAK4", &eta6thAK4, "eta6thAK4/D");
  cutTree->Branch("massTprime", &massTprime, "massTprime/D");
 
  ptAK8 = new std::vector<double>;
  etaAK8 = new std::vector<double>;
  subjAK8 = new std::vector<unsigned>;
  AK8Idx = new std::vector<unsigned>;

  cutTree->Branch("nAK8", &nAK8, "nAK8/i");
  cutTree->Branch("ptAK8", &ptAK8); 
  cutTree->Branch("etaAK8", &etaAK8);
  cutTree->Branch("AK8Idx", &AK8Idx); 

  cutTree->Branch("subjAK8", &subjAK8);

  EvtWeight = new std::vector<double>;

  cutTree->Branch("EvtWeight", &EvtWeight);

  idxHTag = new std::vector<unsigned>;
  idxTTag = new std::vector<unsigned>;
  idxWTag = new std::vector<unsigned>;
  idxbTag = new std::vector<unsigned>;

  cutTree->Branch("HTagIdx", &idxHTag);  
  cutTree->Branch("TTagIdx", &idxTTag);  
  cutTree->Branch("WTagIdx", &idxTTag);  
  cutTree->Branch("bTagIdx", &idxbTag);

  cutTree->Branch("b2AK8Jets",&b2AK8Jets,"b2AK8Jets/O");
  cutTree->Branch("bx2AK8Jets",&bx2AK8Jets,"bx2AK8Jets/O");
  cutTree->Branch("b6AK4Jets",&b6AK4Jets,"b6AK4Jets/O");
  cutTree->Branch("b2AK4Jets",&b2AK4Jets,"b2AK4Jets/O");
  cutTree->Branch("b1AK4Jets",&b1AK4Jets,"b1AK4Jets/O");
  cutTree->Branch("bTMass",&bTMass,"bTMass/O");
  cutTree->Branch("bHMass",&bHMass,"bHMass/O");
  cutTree->Branch("bHTag",&bHTag,"bHTag/O");
  cutTree->Branch("bTTag",&bTTag,"bTTag/O");
  cutTree->Branch("bTTagSubj",&bTTagSubj,"bTTagSubj/O");
  cutTree->Branch("bLoose1",&bLoose1,"bLoose1/O");
  cutTree->Branch("bMedium1",&bMedium1,"bMedium1/O");
  cutTree->Branch("bTight1",&bTight1,"bTight1/O");
  cutTree->Branch("bAK4LeadingPt",&bAK4LeadingPt,"bAK4LeadingPt/O");
  cutTree->Branch("bMass2AK8_1200",&bMass2AK8_1200,"bMass2AK8_1200/O");
  cutTree->Branch("bMass2AK8_1700",&bMass2AK8_1700,"bMass2AK8_1700/O");
  cutTree->Branch("bSoftDropMassAK8",&bSoftDropMassAK8,"bSoftDropMassAK8/O");
  cutTree->Branch("bTrimmedMassAK8",&bTrimmedMassAK8,"bTrimmedMassAK8/O");
  cutTree->Branch("brelM",&brelM,"brelM/O");
  cutTree->Branch("brelpt",&brelpt,"brelpt/O");
  cutTree->Branch("bForwardJet",&bForwardJet,"bForwardJet/O");

  cutTree->Branch("relM",&relM,"relM/D");
  cutTree->Branch("relpt",&relpt,"relpt/D");
  cutTree->Branch("fMaxEtaAK4",&fMaxEtaAK4, "fMaxEtaAK4/D");
  cutTree->Branch("htak4",&htak4, "htak4/D");

  bTrigger = new std::vector<bool>;
  cutTree->Branch("bTrigger",&bTrigger);

  cutTree->Branch("looseBTag", &looseBTag, "looseBTag/i");
  cutTree->Branch("mediumBTag", &mediumBTag, "mediumBTag/i");
  cutTree->Branch("tightBTag", &tightBTag, "tightBTag/i");

 

  histos[ "nBTags1" ] = fs->make<TH1F>( "nBTags1", "# of subjet BTags in jet 1" , 5, 0, 5);
  histos[ "nBTags2" ] = fs->make<TH1F>( "nBTags2", "# of subjet BTags in jet 2" , 5, 0, 5);

  histos[ "nHTags_lsubj" ] = fs->make<TH1F>( "nHTags_lsubj", "# of HTags (loose)", 5, 0, 5);
  histos[ "nTTags_lsubj" ] = fs->make<TH1F>( "nTTags_lsubj", "# of TTags (loose)", 5, 0, 5);
  histos[ "nTTags" ] = fs->make<TH1F>( "nTTags", "# of TTags", 5, 0, 5);
  histos[ "nWTags" ] = fs->make<TH1F>( "nWTags", "# of WTags", 5, 0, 5);
  histos[ "nHTags" ] = fs->make<TH1F>( "nHTags", "# of HTags", 5, 0, 5);

  histos[ "relpt" ] = fs->make<TH1F>( "relpt", "Relative p_{t}", 100, 0 , 1);
  histos[ "relM" ] = fs->make<TH1F>( "relM", "Relative Mass", 100, 0 , 1);

  histos[ "Selection" ] = fs->make<TH1F>( "Selection" , "Selection" , 27, 0 ,27); 
  histos[ "Selection2" ] = fs->make<TH1F>( "Selection2" , "Selection2" , 27, 0 ,27); 
  histos[ "AK4JetPt" ] = fs->make<TH1F>( "pt"  , "p_{t}", 500,  0., 1000. );
  histos[ "AK4JetHt" ] = fs->make<TH1F>( "Ht"  , "H_{t}", 1000,  0., 2000. );
  histos[ "AK4Ht" ] = fs->make<TH1F>( "AK4Ht"  , "H_{t}", 1000,  0., 2000. );
  histos[ "AK4Ht_reweight"]= fs->make<TH1F>( "AK4Ht_rew"  , "H_{t}", 1000,  0., 2000. );
  histos[ "AK4trigHt" ] = fs->make<TH1F>( "AK4 trig Ht"  , "H_{t}", 1000,  0., 2000. );
  histos[ "AK8Ht" ] = fs->make<TH1F>( "AK8 Ht"  , "H_{t}", 1000,  0., 2000. );
  histos[ "AK4JetdR" ] = fs->make<TH1F>( "jetdR" , "dR between Jets", 50, 0. ,5.);
  histos[ "AK4JetPairMass" ] = fs->make<TH1F>( "jetPairMass"  , "Jet Pair Mass", 1000,  0., 2000. );
  histos[ "AK4JetFlavor" ] = fs->make<TH1F>( "jetPairFlavor"  , "Jet Pair Flavor", 10,  0., 10. );
  histos[ "AK4BTags-l" ] = fs->make<TH1F>( "jetBTags-l"  , "Jet BTags(loose)", 10,  0., 10. );
  histos[ "AK4BTags-m" ] = fs->make<TH1F>( "jetBTags-m"  , "Jet BTags(medium)", 10,  0., 10. );
  histos[ "AK4BTags-t" ] = fs->make<TH1F>( "jetBTags-t"  , "Jet BTags(tight)", 10,  0., 10. );
  histos[ "AK4Jets" ] = fs->make<TH1F>( "jets"  , "Jets after sel", 10,  0., 10. );

  histos["2AK4Mass"] = fs->make<TH1F>( "MassLeading2AK4","MassLeading2AK4",1000,  0., 2000.); 
  histos["softDropMassAK8"] = fs->make<TH1F>( "softDropMassAK8","softDropMassAK8",500,  0., 500.);
  histos["trimmedMassAK8"] = fs->make<TH1F>( "trimmedMassAK8","trimmedMassAK8",500,  0., 500.);

  histos["ptLeadingAK4"] = fs->make<TH1F>( "ptLeadingAK4","ptLeadingAK4",1000,  0., 2000.);
  histos["etaLeadingAK4"] = fs->make<TH1F>( "etaLeadingAK4","etaLeadingAK4",50,  -5., 5.);
  histos["pt2ndAK4"] = fs->make<TH1F>( "pt2ndAK4","pt2ndAK4",1000,  0., 2000.);
  histos["eta2ndAK4"] = fs->make<TH1F>( "eta2ndAK4","eta2ndAK4",50,  -5., 5.);
  histos["pt3rdAK4"] = fs->make<TH1F>( "pt3rdAK4","pt3rdAK4",1000,  0., 2000.);
  histos["eta3rdAK4"] = fs->make<TH1F>( "eta3rdAK4","eta3rdAK4",50,  -5., 5.);
  histos["pt4thAK4"] = fs->make<TH1F>( "pt4thAK4","pt4thAK4",1000,  0., 2000.);
  histos["eta4thAK4"] = fs->make<TH1F>( "eta4thAK4","eta4thAK4",50,  -5., 5.);
  histos["pt5thAK4"] = fs->make<TH1F>( "pt5thAK4","pt5thAK4",1000,  0., 2000.);
  histos["eta5thAK4"] = fs->make<TH1F>( "eta5thAK4","eta5thAK4",50,  -5., 5.);
  histos["pt6thAK4"] = fs->make<TH1F>( "pt6thAK4","pt6thAK4",1000,  0., 2000.);
  histos["eta6thAK4"] = fs->make<TH1F>( "eta6thAK4","eta6thAK4",50,  -5., 5.);

  histos["eta1stAK8"] = fs->make<TH1F>( "eta1stAK4","eta1stAK4",50,  -5., 5.);
  histos["eta2ndAK8"] = fs->make<TH1F>( "eta2ndAK8","eta2ndAK4",50,  -5., 5.);

  histos["dPhiLeadingAK8"] = fs->make<TH1F>( "dPhiLeadingAK8" , "dPhiLeadingAK8", 80, 0. ,4.);

  histos[ "ngoodAK4Jets" ] = fs->make<TH1F>( "ngoodAK4Jets"  , "AK4 Jets after sel", 20,  0., 20. );
  histos[ "ngoodAK8Jets" ] = fs->make<TH1F>( "ngoodAK8Jets"  , "AK8 Jets after sel", 20,  0., 20. );
  histos[ "ngoodAK4Jets_Unm"] = fs->make<TH1F>( "ngoodAK4Jets_Unm"  , "AK4 Jets (unmatched) after sel", 20,  0., 20. );
  histos[ "ngoodAK4Jets_Unm_presel"] = fs->make<TH1F>( "ngoodAK4Jets_Unm_presel"  , "AK4 Jets (unmatched) after presel", 20,  0., 20. );

  histos[ "HT_presel" ] = fs->make<TH1F>( "HT_presel" ,"H_{t} after preselection", 1000,  0., 2000. );
  histos[ "pt1stAK8_presel" ] = fs->make<TH1F>( "pt1stAK8_presel" ,"p_{t} Leading AK8 after preselection", 1000,  0., 2000. );
  histos[ "eta1stAK8_presel" ] = fs->make<TH1F>( "eta1stAK8_presel","eta Leading AK8 after preselection ",50,  -5., 5.);
  histos[ "pt2ndAK8_presel" ] = fs->make<TH1F>( "pt2ndAK8_presel" ,"p_{t} 2nd AK8 after preselection", 1000,  0., 2000. );
  histos[ "eta2ndAK8_presel" ] = fs->make<TH1F>( "eta2ndAK8_presel","eta 2nd AK8 after preselection ",50,  -5., 5.);

  // AK4 stuff
  histos["ptLeadingAK4_presel"] = fs->make<TH1F>( "ptLeadingAK4_presel","p_{t} Leading AK4 after preselection",1000,  0., 2000.);
  histos["etaLeadingAK4_presel"] = fs->make<TH1F>( "etaLeadingAK4_presel","eta Leading AK4 after preselection",50,  -5., 5.);
  histos["pt2ndAK4_presel"] = fs->make<TH1F>( "pt2ndAK4_presel","p_{t} 2nd AK4 after preselection",1000,  0., 2000.);
  histos["eta2ndAK4_presel"] = fs->make<TH1F>( "eta2ndAK4_presel","eta 2nd AK4 after preselection",50,  -5., 5.);
  histos[ "maxetaAK4_presel" ]= fs->make<TH1F>("maxetaAK4_presel","Max eta for AK4 after preselection",50, 0. ,5. );
  


  histos [ "BtagsAK4_t_presel" ] = fs->make<TH1F>("BtagsAK4_t_presel"  , "# of Tight Btags (AK4)", 100,  0., 10. );
  histos [ "relM_presel" ] = fs->make<TH1F>("relM_presel" , "Relative Mass (AK8)" , 100, 0 ,1); 
  histos [ "TprimeMass_presel" ] = fs->make<TH1F>("TprimeMass_presel", "Tprime Candidate Mass (2AK8)", 1000,0,2000);
  histos [ "softDropMass_presel" ] = fs->make<TH1F>("softDropMass_presel", "SoftDropMass (Leading AK8)", 1000,0,2000);

  histos [ "BtagsAK4_t_sel" ] = fs->make<TH1F>("BtagsAK4_t_sel"  , "# of Tight Btags (AK4)", 100,  0., 10. );
  histos [ "relM_sel" ] = fs->make<TH1F>("relM_sel" , "Relative Mass (AK8)" , 100, 0 ,1); 
  histos [ "TprimeMass_sel" ] = fs->make<TH1F>("TprimeMass_sel", "Tprime Candidate Mass (2AK8)", 1000,0,2000);
  histos [ "softDropMass_sel" ] = fs->make<TH1F>("softDropMass_sel", "SoftDropMass (Leading AK8)",1000, 0, 2000);
  histos[ "maxetaAK4_sel" ]= fs->make<TH1F>("maxetaAK4_sel","Max eta for AK4 after Selection",50, 0. ,5. );


 // histos[ "nlooseBTaggedAK4Jets" ] = fs->make<TH1F>( "nlooseBTaggedAK4Jets"  , "Jets after sel", 10,  0., 10.  );
  histos[ "nWJets" ] = fs->make<TH1F>("nWJets"  , "nWJets", 10,  0., 10. );
  histos[ "nHJets" ] = fs->make<TH1F>("nHJets"  , "nHJets", 10,  0., 10. );
  histos[ "maxetaak4" ]= fs->make<TH1F>("maxetaak4","maxetaak4",50, 0. ,5. );
  histos[ "MassLeading2AK8" ]= fs->make<TH1F>( "MassLeading2AK8","MassLeading2AK8",1000,  0., 2000.);
  histos[ "DeltaEtaLeading2AK8" ]= fs->make<TH1F>("deltaetaak8","delta eta ak8 ", 100, 0 ,10);
  histos[ "pt1stAK8" ]= fs->make<TH1F>("pt1stAK8","pt1stAK8", 1000,  0., 2000.);
  histos[ "pt2ndAK8" ]= fs->make<TH1F>("pt2ndAK8","pt2ndAK8", 1000,  0., 2000.);
  histos[ "mass1stAK8" ]= fs->make<TH1F>( "mass1stAK8","mass1stAK8",1000,  0., 2000.);
  histos[ "mass2ndAK8" ]= fs->make<TH1F>( "mass2ndAK8","mass2ndAK8",1000,  0., 2000.);

  histos[ "ak4tMatched" ]= fs->make<TH1F>( "ak4tMatched","ak4tMatched",3,0,3);
  histos[ "ak4hMatched" ]= fs->make<TH1F>( "ak4hMatched","ak4hMatched",3,0,3);
  histos[ "ak8tMatched" ]= fs->make<TH1F>( "ak8tMatched","ak8tMatched",3,0,3);
  histos[ "ak8hMatched" ]= fs->make<TH1F>( "ak8hMatched","ak8hMatched",3,0,3);
 
  histos[ "ak8tMatchedMass" ]= fs->make<TH1F>( "ak8tMatchedMass","ak8tMatchedMass",300,0,300);
  histos[ "ak8hMatchedMass" ]= fs->make<TH1F>( "ak8hMatchedMass","ak8hMatchedMass",300,0,300);

  //histos[ "drHiggs" ] = fs->make<TH1F>( "drHiggs","drHiggs",

  histos[ "SidebandA-M" ]= fs->make<TH1F>( "SidebandA","SidebandA" ,1000,  0., 4000.);
  histos[ "SidebandB-M" ]= fs->make<TH1F>( "SidebandB","SidebandB" ,1000,  0., 4000.);
  histos[ "SidebandC-M" ]= fs->make<TH1F>( "SidebandC","SidebandC" ,1000,  0., 4000.);
  histos[ "SidebandD-M" ]= fs->make<TH1F>( "SidebandD","SidebandD" ,1000,  0., 4000.);

  histos[ "DEstimate-M" ]= fs->make<TH1F>( "DEstimate","DEstimate" ,1000,  0., 4000.);

  histos[ "SidebandA-HT" ]= fs->make<TH1F>( "SidebandA-HT","SidebandA-HT" ,1000,  0., 4000.);
  histos[ "SidebandB-HT" ]= fs->make<TH1F>( "SidebandB-HT","SidebandB-HT" ,1000,  0., 4000.);
  histos[ "SidebandC-HT" ]= fs->make<TH1F>( "SidebandC-HT","SidebandC-HT" ,1000,  0., 4000.);
  histos[ "SidebandD-HT" ]= fs->make<TH1F>( "SidebandD-HT","SidebandD-HT" ,1000,  0., 4000.);

  histos[ "DEstimate-HT" ]= fs->make<TH1F>( "DEstimate-HT","DEstimate-HT" ,1000,  0., 4000.);

  histos[ "HTagCandidateMass" ] = fs->make<TH1F>( "HTagCandidateMass", "Higgs Candidate Mass ( Tagger )",300,0,300 );
  histos[ "HCandidateMass" ] = fs->make<TH1F>( "HCandidateMass", "Higgs Candidate Mass ( AK8 ( 2subjets )",300,0,300 );

  histos["2AK8_AK4CSV"] = fs->make<TH1F>( "2AK8_AK4CSV", "AK4 CSV Unmatched (2AK8)",100,0,1 );
  histos["2AK8_AK4pt"] = fs->make<TH1F>( "2AK8_AK4pt", "AK4 pt Unmatched (2AK8)",1000,0,2000 );
  histos["2AK8_AK4eta"] = fs->make<TH1F>( "2AK8_AK4eta", "AK4 eta Unmatched (2AK8)",100,-5,5 );
  histos["2AK8_nAK4"] =fs->make<TH1F>( "2AK8_nAK4", "Number of AK4 Unmatched (2AK8)",20,0,20 );

  histos2["HvsT"] = fs->make<TH2F>( "HvsT", "HTags vs. TTags", 5, 0, 5,5,0,5);

  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(1,"Preselection" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(2,"b2AK8Jets" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(3,"b2AK8Jets && b5AK4Jets" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(4,"b2AK8Jets && b5AK4Jets && bLoose2" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(5,"b2AK8Jets && b5AK4Jets && bLoose2 && bTTag" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(6,"b2AK8Jets && b5AK4Jets && bLoose3" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(7,"b2AK8Jets && b5AK4Jets && bLoose3 && bTTag" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(8,"b2AK8Jets && b5AK4Jets && bLoose2 && bForwardJet" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(9,"b2AK8Jets && b5AK4Jets && bLoose3 && bForwardJet" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(10,"b2AK8Jets && b2AK4Jets && bLoose2" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(11,"b2AK8Jets && b2AK4Jets && bLoose2 && bForwardJet" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(12,"b2AK8Jets && b2AK4Jets && bLoose2 && bTTag && bForwardJet" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(13,"b2AK8Jets && b5AK4Jets && bLoose3 && bTTag && bForwardJet" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(14,"b2AK8Jets && b5AK4Jets && bLoose3 && brelpt && brelM" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(15,"b2AK8Jets && b5AK4Jets && bLoose3 && bForwardJet && brelpt && brelM" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(16,"b1AK8Jets && b4AK4Jets && brelpt && brelM" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(17,"b1AK8Jets && b4AK4Jets && bForwardJet && brelpt && brelM" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(18,"b1AK8Jets && b4AK4Jets && bLoose2 && brelpt && brelM" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(19,"b1AK8Jets && b4AK4Jets && bLoose2 && bForwardJet && brelpt && brelM" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(20,"b2AK8Jets && b4AK4Jets && bForwardJet && brelpt && brelM" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(21,"b2AK8Jets && b4AK4Jets && bLoose2 && brelpt && brelM" );
  histos[ "Selection2" ]->GetXaxis()->SetBinLabel(22,"b2AK8Jets && b4AK4Jets && bLoose2 && bForwardJet && brelpt && brelM" );

  histos[ "Selection" ]->GetXaxis()->SetBinLabel(1,"Preselection" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(2,"b2AK8Jets" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(3,"b2AK8Jets && b2AK4Jets" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(4,"b2AK8Jets && bTTag" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(5,"b2AK8Jets && bMedium1" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(6,"b2AK8Jets && bHTag" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(7,"b2AK8Jets && bForwardJet" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(8,"b2AK8Jets && brelpt" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(9,"b2AK8Jets && brelM" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(10,"b2AK8Jets && bAK4LeadingPt" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(11,"b2AK8Jets && bSoftDropMassAK8" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(12,"b2AK8Jets && bTrimmedMassAK8" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(13,"b2AK8Jets && bLoose1" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(14,"b2AK8Jets && bTight1" );
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(15,"b2AK8Jets && b1AK4Jets");

  histos[ "Selection" ]->GetXaxis()->SetBinLabel(16,"b2AK8Jets && bdPhiAK8");
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(17,"b2AK8Jets && bMass2AK8_1200");
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(18,"b2AK8Jets && bMass2AK8_1700");

  histos[ "Selection" ]->GetXaxis()->SetBinLabel(19,"b2AK8Jets && bTight1 && bHTag && bTTag && brelM && bSoftDropMassAK8 && bMass2AK8_1200");
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(20,"b2AK8Jets && bTight1 && bHTag && bTTag && brelM && bSoftDropMassAK8 && bMass2AK8_1700");

  

}



// ------------ method called once each job just after ending the event loop  ------------
void 
TprimeAna::endJob() 

{
	//std::cout << "endjob" << std::endl; 

	for( unsigned int i = 1; i < 1000; i++ )
	{
		int A = histos[ "SidebandA-M" ]->GetBinContent(i);
		int B = histos[ "SidebandB-M" ]->GetBinContent(i);
		int C = histos[ "SidebandC-M" ]->GetBinContent(i);
		if(A != 0 )  	histos[ "DEstimate-M" ]->SetBinContent(i,B*C/A);
		
		A = histos[ "SidebandA-HT" ]->GetBinContent(i);
		B = histos[ "SidebandB-HT" ]->GetBinContent(i);
		C = histos[ "SidebandC-HT" ]->GetBinContent(i);
		if(A != 0 )  	histos[ "DEstimate-HT" ]->SetBinContent(i,B*C/A);
	}

}

// ------------ method called when starting to processes a run  ------------
/*
void 
TprimeAna::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
TprimeAna::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
TprimeAna::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
TprimeAna::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
TprimeAna::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(TprimeAna);
