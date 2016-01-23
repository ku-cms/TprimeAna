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
#include <TObject.h>
//#include "AK8Jets.h"



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
      bool _isTTJets;
      edm::InputTag l_trigName;
      edm::InputTag l_trigBit;
      std::vector<std::string> hltPaths_  ;


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


        double softDropMassLeadAK8; 
        double trimmedMassLeadAK8; 
	double massTprime;
	

	const int * npv, * puNtrueInt;	

	std::vector<double> * ptAK4;
	std::vector<double> * etaAK4;
	std::vector<double> * phiAK4;
	std::vector<double> * ptAK8;
	std::vector<double> * etaAK8;
	std::vector<double> * phiAK8;
	std::vector<double> * MAK8;
	std::vector<double> * MAK4;
	std::vector<double> * SoftDropMassAK8;
	std::vector<double> * PrunedMassAK8;
	std::vector<double> * tau1AK8;
	std::vector<double> * tau2AK8;
	std::vector<double> * tau3AK8;

	std::vector<unsigned> * idxAK4;
	std::vector<unsigned> * idxAK8;
//	std::vector<unsigned> * AK4UnmatchedIdx;	
	std::vector<unsigned> * AK4UnmatchedIdx03;	
//	std::vector<unsigned> * AK4UnmatchedIdx10;	
//	std::vector<unsigned> * AK4UnmatchedIdx30;	

	std::vector<double> * EvtWeight;

	std::vector<unsigned> * idxHTag;
	std::vector<unsigned> * idxHTagSB0;
	std::vector<unsigned> * idxHTagSB1;
//	std::vector<unsigned> * idxTTagsub;
//	std::vector<unsigned> * idxTTagsub2;
//	std::vector<unsigned> * idxTTag;
//	std::vector<unsigned> * idxTTag03sub;
	std::vector<unsigned> * idxTTag03;
	std::vector<unsigned> * idxTTag03SB0;
//	std::vector<unsigned> * idxTTag10;
//	std::vector<unsigned> * idxTTag30;
//	std::vector<unsigned> * idxTTag0;
//	std::vector<unsigned> * idxTTag1;
//	std::vector<unsigned> * idxTTag2;
//	std::vector<unsigned> * idxTTag3;
	std::vector<unsigned> * idxWTag;
	std::vector<unsigned> * idxbTag;

	std::vector<unsigned> * subjAK8;
	std::vector<float> * sj0IdxAK8;
	std::vector<float> * sj1IdxAK8;
	std::vector<float> * sj2IdxAK8;
	std::vector<float> * sj3IdxAK8;

	std::vector<float> * sjCSVAK8;
	std::vector<float> * sjCSVV1AK8;

	unsigned nAK8;

	bool bTrigger;

        double relM, relpt;
        unsigned looseBTag, mediumBTag, tightBTag;

	double htak4, htak8, fMaxEtaAK4;
	
	int  inpv, ipuNtrueInt;

	TH1D * PUcorr;
	
//	AK8Jets * ak8s;

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
	_isTTJets               (iConfig.getParameter<bool>              ("isTTJets")),
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
      edm::Handle<int> mh_npv;
      edm::Handle<int> mh_puNtrueInt;
      edm::Handle<double> mh_TTBarWeight;

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
      edm::Handle<std::vector<float> > mh_jetAK8vsubjetIndex0;
      edm::Handle<std::vector<float> > mh_jetAK8vsubjetIndex1;
      edm::Handle<std::vector<float> > mh_jetAK8topsubjetIndex0;
      edm::Handle<std::vector<float> > mh_jetAK8topsubjetIndex1;
      edm::Handle<std::vector<float> > mh_jetAK8topsubjetIndex2;
      edm::Handle<std::vector<float> > mh_jetAK8topsubjetIndex3;
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

      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagPt;
      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagEta;
      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagPhi;
      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagE;
      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagMass;
      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagHadronFlavour;
      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagtau1;
      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagtau2;
      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagtau3;

      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagCSV;
      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagCSVV1;

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
      edm::Handle<std::vector<unsigned> > mh_ak4UnmatchedIdx03;
      edm::Handle<std::vector<unsigned> > mh_ak4UnmatchedIdx10;
      edm::Handle<std::vector<unsigned> > mh_ak4UnmatchedIdx30;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdxsub;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdxsub2;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx03sub;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx03;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx03SB0;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx10;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx30;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx0;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx1;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx2;
      edm::Handle<std::vector<unsigned> > mh_tjetsIdx3;
      edm::Handle<std::vector<unsigned> > mh_hjetsIdx;
      edm::Handle<std::vector<unsigned> > mh_hjetsIdxSB0;
      edm::Handle<std::vector<unsigned> > mh_hjetsIdxSB1;

      edm::Handle<double> mh_maxetaak4;
      edm::Handle<double> mh_MassLeading2AK8;
      edm::Handle<double> mh_DeltaEtaLeading2AK8;
      edm::Handle<double> mh_pt1stAK8;
      edm::Handle<double> mh_pt2ndAK8;
      edm::Handle<double> mh_mass1stAK8;
      edm::Handle<double> mh_mass2ndAK8;

      edm::Handle<vector<string> > h_trigName             ; iEvent.getByLabel (l_trigName               , h_trigName             );
      edm::Handle<vector<float> > h_trigBit              ; iEvent.getByLabel (l_trigBit                , h_trigBit              );

      edm::Handle<vector<double> > mh_EvtWeight;


      iEvent.getByLabel("eventInfo", "evtInfoEventNumber", mh_evtNum);
      iEvent.getByLabel("eventUserData", "npv", mh_npv) ;  
      iEvent.getByLabel("eventUserData", "puNtrueInt", mh_puNtrueInt);   
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

//      iEvent.getByLabel("anavars", "ak4UnmatchedIdx",mh_ak4UnmatchedIdx);
      iEvent.getByLabel("anavars", "ak4UnmatchedIdx03",mh_ak4UnmatchedIdx03);
//      iEvent.getByLabel("anavars", "ak4UnmatchedIdx10",mh_ak4UnmatchedIdx10);
//      iEvent.getByLabel("anavars", "ak4UnmatchedIdx30",mh_ak4UnmatchedIdx30);
//      iEvent.getByLabel("anavars", "tjetsIdx03sub",mh_tjetsIdx03sub);
      iEvent.getByLabel("anavars", "tjetsIdx03",mh_tjetsIdx03);
      iEvent.getByLabel("anavars", "tjetsIdx03sb0",mh_tjetsIdx03SB0);
//      iEvent.getByLabel("anavars", "tjetsIdx10",mh_tjetsIdx10);
//      iEvent.getByLabel("anavars", "tjetsIdx30",mh_tjetsIdx30);
//      iEvent.getByLabel("anavars", "tjetsIdxsub2",mh_tjetsIdxsub2);
//      iEvent.getByLabel("anavars", "tjetsIdxsub",mh_tjetsIdxsub);
//      iEvent.getByLabel("anavars", "tjetsIdx",mh_tjetsIdx);
//      iEvent.getByLabel("anavars", "tjetsIdx0",mh_tjetsIdx0);
//      iEvent.getByLabel("anavars", "tjetsIdx1",mh_tjetsIdx1);
//      iEvent.getByLabel("anavars", "tjetsIdx2",mh_tjetsIdx2);
//      iEvent.getByLabel("anavars", "tjetsIdx3",mh_tjetsIdx3);
      iEvent.getByLabel("anavars", "hjetsIdx",mh_hjetsIdx);
      iEvent.getByLabel("anavars", "hjetsIdxSB0",mh_hjetsIdxSB0);
      iEvent.getByLabel("anavars", "hjetsIdxSB1",mh_hjetsIdxSB1);
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

      if(_isTTJets)
	iEvent.getByLabel("TopPt","TTBarWeight",mh_TTBarWeight);

      iEvent.getByLabel("jetsAK8", "jetAK8Pt", mh_jetAK8Pt);
      iEvent.getByLabel("jetsAK8", "jetAK8Eta", mh_jetAK8Eta);
      iEvent.getByLabel("jetsAK8", "jetAK8Phi", mh_jetAK8Phi);
      iEvent.getByLabel("jetsAK8", "jetAK8E", mh_jetAK8E);
      iEvent.getByLabel("jetsAK8", "jetAK8Mass", mh_jetAK8Mass);
      iEvent.getByLabel("jetsAK8", "jetAK8vSubjetIndex0", mh_jetAK8vsubjetIndex0);
      iEvent.getByLabel("jetsAK8", "jetAK8vSubjetIndex1", mh_jetAK8vsubjetIndex1);
      iEvent.getByLabel("jetsAK8", "jetAK8topSubjetIndex0", mh_jetAK8topsubjetIndex0);
      iEvent.getByLabel("jetsAK8", "jetAK8topSubjetIndex1", mh_jetAK8topsubjetIndex1);
      iEvent.getByLabel("jetsAK8", "jetAK8topSubjetIndex2", mh_jetAK8topsubjetIndex2);
      iEvent.getByLabel("jetsAK8", "jetAK8topSubjetIndex3", mh_jetAK8topsubjetIndex3);
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

      iEvent.getByLabel("subjetsCmsTopTag", "subjetsCmsTopTagPt", mh_subjetsCmsTopTagPt);
      iEvent.getByLabel("subjetsCmsTopTag", "subjetsCmsTopTagEta", mh_subjetsCmsTopTagEta);
      iEvent.getByLabel("subjetsCmsTopTag", "subjetsCmsTopTagPhi", mh_subjetsCmsTopTagPhi);
      iEvent.getByLabel("subjetsCmsTopTag", "subjetsCmsTopTagE", mh_subjetsCmsTopTagE);
      iEvent.getByLabel("subjetsCmsTopTag", "subjetsCmsTopTagMass", mh_subjetsCmsTopTagMass);
      iEvent.getByLabel("subjetsCmsTopTag", "subjetsCmsTopTagHadronFlavour", mh_subjetsCmsTopTagHadronFlavour);
      iEvent.getByLabel("subjetsCmsTopTag", "subjetsCmsTopTagtau1", mh_subjetsCmsTopTagtau1);
      iEvent.getByLabel("subjetsCmsTopTag", "subjetsCmsTopTagtau2", mh_subjetsCmsTopTagtau2);
      iEvent.getByLabel("subjetsCmsTopTag", "subjetsCmsTopTagtau3", mh_subjetsCmsTopTagtau3);
      
      iEvent.getByLabel("subjetsCmsTopTag", "subjetCmsTopTagCSV", mh_subjetsCmsTopTagCSV);
      iEvent.getByLabel("subjetsCmsTopTag", "subjetCmsTopTagCSVV1",mh_subjetsCmsTopTagCSVV1);

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
      npv = mh_npv.product();
      puNtrueInt = mh_puNtrueInt.product();

      inpv = *npv;
      ipuNtrueInt = *puNtrueInt;

      const double * TTBarWeight;

      if(_isTTJets )
          TTBarWeight = mh_TTBarWeight.product();

//      const std::vector<float> * jetcsv = mh_jetAK4CSV.product();
      const std::vector<float> * jet4pt = mh_jetAK4Pt.product();
      const std::vector<float> * jet4eta = mh_jetAK4Eta.product();
      const std::vector<float> * jet4phi = mh_jetAK4Phi.product();
      const std::vector<float> * jet4M = mh_jetAK4Mass.product();
//      const std::vector<float> * jet4flavor = mh_jetAK4HadronFlavour.product();
      const std::vector<unsigned> * jetgood = mh_jetAK4Good.product();
      const std::vector<float> * jet4CSV = mh_jetAK4CSV.product();
//      const unsigned * nAK4Unmatched = mh_nAk4Unmatched.product();
//     const std::vector<unsigned> * ak4UnmatchedIdx = mh_ak4UnmatchedIdx.product();
     const std::vector<unsigned> * ak4UnmatchedIdx03 = mh_ak4UnmatchedIdx03.product();
//     const std::vector<unsigned> * ak4UnmatchedIdx10 = mh_ak4UnmatchedIdx10.product();
//     const std::vector<unsigned> * ak4UnmatchedIdx30 = mh_ak4UnmatchedIdx30.product();

      const std::vector<float> * jet8pt = mh_jetAK8Pt.product();
      const std::vector<float> * jet8eta = mh_jetAK8Eta.product();
      const std::vector<float> * jet8phi = mh_jetAK8Phi.product();
      const std::vector<float> * jet8M = mh_jetAK8Mass.product();
      const std::vector<float> * jet8nSubjets = mh_jetAK8nSubjets.product();
      const std::vector<unsigned> * jet8good = mh_jetAK8Good.product();
      const std::vector<float> * softDropMassAK8 = mh_jetAK8SoftDropMass.product();
      const std::vector<float> * trimmedMassAK8 = mh_jetAK8TrimmedMass.product();
      const std::vector<float> * prunedMassAK8 = mh_jetAK8PrunedMass.product();
      const std::vector<float> * jet8Tau1 = mh_jetAK8tau1.product();	
      const std::vector<float> * jet8Tau2 = mh_jetAK8tau2.product();	
      const std::vector<float> * jet8Tau3 = mh_jetAK8tau3.product();	
//      const std::vector<float> * jetAK8vsubjetIndex0 = mh_jetAK8vsubjetIndex0.product();
//      const std::vector<float> * jetAK8vsubjetIndex1 = mh_jetAK8vsubjetIndex1.product();
      const std::vector<float> * jetAK8topsubjetIndex0 = mh_jetAK8topsubjetIndex0.product();
      const std::vector<float> * jetAK8topsubjetIndex1 = mh_jetAK8topsubjetIndex1.product();
      const std::vector<float> * jetAK8topsubjetIndex2 = mh_jetAK8topsubjetIndex2.product();
      const std::vector<float> * jetAK8topsubjetIndex3 = mh_jetAK8topsubjetIndex3.product();

      const std::vector<float> * subjet8CSVV1 = mh_subjetsCmsTopTagCSVV1.product();
      const std::vector<float> * subjet8CSV = mh_subjetsCmsTopTagCSV.product();


      const std::vector<unsigned> * tjetsIdx03 = mh_tjetsIdx03.product();
      const std::vector<unsigned> * tjetsIdx03SB0 = mh_tjetsIdx03SB0.product();
//      const std::vector<unsigned> * tjetsIdx03sub = mh_tjetsIdx03sub.product();
//      const std::vector<unsigned> * tjetsIdx10 = mh_tjetsIdx10.product();
//      const std::vector<unsigned> * tjetsIdx30 = mh_tjetsIdx30.product();
//      const std::vector<unsigned> * tjetsIdxsub = mh_tjetsIdxsub.product();
//      const std::vector<unsigned> * tjetsIdxsub2 = mh_tjetsIdxsub2.product();
//      const std::vector<unsigned> * tjetsIdx = mh_tjetsIdx.product();
//      const std::vector<unsigned> * tjetsIdx0 = mh_tjetsIdx0.product();
//      const std::vector<unsigned> * tjetsIdx1 = mh_tjetsIdx1.product();
//      const std::vector<unsigned> * tjetsIdx2 = mh_tjetsIdx2.product();
//      const std::vector<unsigned> * tjetsIdx3 = mh_tjetsIdx3.product();

      const std::vector<unsigned> * hjetsIdx = mh_hjetsIdx.product();
      const std::vector<unsigned> * hjetsIdxSB0 = mh_hjetsIdxSB0.product();
      const std::vector<unsigned> * hjetsIdxSB1 = mh_hjetsIdxSB1.product();
      const std::vector<unsigned> * wjetsIdx = mh_wjetsIdx.product();

      const std::vector<unsigned> * bjetsIdx = mh_bjetsIdx.product();


/*
      const std::vector<float> * genPartID = mh_genPartID.product();
      const std::vector<float> * genPartMomID = mh_genPartMom0ID.product();
      const std::vector<float> * genPartStatus= mh_genPartStatus.product();
      const std::vector<float> * genPartEta = mh_genPartEta.product();
      const std::vector<float> * genPartPhi = mh_genPartPhi.product();
*/
      const double * htak4jets = mh_htak4jets.product();
      htak4 = *htak4jets;

//      const double * htak4trigjets = mh_htak4trigjets.product();
      const double * htak8jets = mh_htak8jets.product();
      htak8 = *htak8jets;

//      const unsigned * ngoodAK4Jets = mh_ngoodAK4Jets.product();
      const unsigned * ngoodAK8Jets = mh_ngoodAK8Jets.product();

//      const ULong64_t * evtNum = mh_evtNum.product();
	
//	cout << "EvtWeight" << endl;

      const std::vector<double> * EvtWeight_;

      if(!_isData) EvtWeight_ = mh_EvtWeight.product();
	else {
		EvtWeight_ = new std::vector<double>{1};
	}

	

			
//     Trigger

  bTrigger = false;
  for ( unsigned int i = 0 ; i < h_trigName.product()->size() ; i++ ) {

        //Support regex pattern matching: wildcards . and .*
        //
       // cout << hltPaths_.size()<<endl;
       for( unsigned int j = 0; j < hltPaths_.size() ; j++ ) {

           string hltname = h_trigName.product()->at(i);
           boost::regex pattern(hltPaths_[j]);

           if(boost::regex_match(hltname , pattern)>0) {
		bTrigger = (h_trigBit.product()->at(i)>0);
       //         cout << hltname << "  " << hltPaths_[j] << "  " << bTrigger << endl;
	   }


       }
   }



	//cout << "Clear" << endl;
   nAK8 = (*ngoodAK8Jets);

   tau1AK8->clear();	
   tau2AK8->clear();	
   tau3AK8->clear();	
   subjAK8->clear();
   idxHTag->clear();
   idxHTagSB0->clear();
   idxHTagSB1->clear();
//   idxTTag->clear();
//   idxTTagsub->clear();
//   idxTTagsub2->clear();
   idxTTag03->clear();
   idxTTag03SB0->clear();
//   idxTTag03sub->clear();
//   idxTTag10->clear();
//   idxTTag30->clear();
//   idxTTag0->clear();
//   idxTTag1->clear();
//   idxTTag2->clear();
//   idxTTag3->clear();
   ptAK8->clear();
   etaAK8->clear();
   phiAK8->clear();
   MAK8->clear();
   SoftDropMassAK8->clear();
   PrunedMassAK8->clear();
   ptAK4->clear();
   etaAK4->clear();
   phiAK4->clear();
   MAK4->clear();
   EvtWeight->clear();
   idxAK4->clear();
   idxAK8->clear();
   idxWTag->clear();
   idxbTag->clear();
//   AK4UnmatchedIdx->clear();
   AK4UnmatchedIdx03->clear();
//   AK4UnmatchedIdx10->clear();
//   AK4UnmatchedIdx30->clear();

   sj0IdxAK8->clear();
   sj1IdxAK8->clear();
   sj2IdxAK8->clear();
   sj3IdxAK8->clear();
   sjCSVAK8->clear();
   sjCSVV1AK8->clear();

	for (unsigned i = 0 ; i < jet8pt->size() ; i++) {
	    ptAK8->push_back((*jet8pt)[i]);
	    etaAK8->push_back((*jet8eta)[i]);
	    phiAK8->push_back((*jet8phi)[i]);
	    MAK8->push_back((*jet8M)[i]);
	    subjAK8->push_back((*jet8nSubjets)[i]);
      	    sj0IdxAK8->push_back((*jetAK8topsubjetIndex0)[i]);
      	    sj1IdxAK8->push_back((*jetAK8topsubjetIndex1)[i]); 
      	    sj2IdxAK8->push_back((*jetAK8topsubjetIndex2)[i]); 
      	    sj3IdxAK8->push_back((*jetAK8topsubjetIndex3)[i]); 
	    PrunedMassAK8->push_back((*prunedMassAK8)[i]);
	    SoftDropMassAK8->push_back((*softDropMassAK8)[i]);
	    tau1AK8->push_back((*jet8Tau1)[i]);
	    tau2AK8->push_back((*jet8Tau2)[i]);
	    tau3AK8->push_back((*jet8Tau3)[i]);
	}

	for (unsigned i = 0 ; i < jet4pt->size() ; i++) {
	    ptAK4->push_back((*jet4pt)[i]);
	    etaAK4->push_back((*jet4eta)[i]);
	    phiAK4->push_back((*jet4phi)[i]);
	    MAK4->push_back((*jet4M)[i]);
	}
	//cout << "AK8" <<endl;
//	ak8s->Load(jet8pt,jet8eta,jet8phi,jet8M);

	sjCSVV1AK8->reserve(subjet8CSVV1->size());
	sjCSVAK8->reserve(subjet8CSV->size());

	//cout << "reserve"<< endl;

	idxHTag->reserve(hjetsIdx->size());
	idxHTagSB0->reserve(hjetsIdxSB0->size());
	idxHTagSB1->reserve(hjetsIdxSB1->size());
//	idxTTagsub->reserve(tjetsIdxsub->size());
//	idxTTagsub2->reserve(tjetsIdxsub2->size());
//	idxTTag->reserve(tjetsIdx->size());
//	idxTTag03sub->reserve(tjetsIdx03sub->size());
	idxTTag03->reserve(tjetsIdx03->size());
	idxTTag03SB0->reserve(tjetsIdx03SB0->size());
//	idxTTag10->reserve(tjetsIdx10->size());
//	idxTTag30->reserve(tjetsIdx30->size());
//	idxTTag0->reserve(tjetsIdx0->size());
//	idxTTag1->reserve(tjetsIdx1->size());
//	idxTTag2->reserve(tjetsIdx2->size());
//	idxTTag3->reserve(tjetsIdx3->size());
	idxWTag->reserve(wjetsIdx->size());
	EvtWeight->reserve(EvtWeight_->size());
	idxbTag->reserve(bjetsIdx->size());
	idxAK4->reserve(jetgood->size());
	idxAK8->reserve(jet8good->size());
//	AK4UnmatchedIdx->reserve( ak4UnmatchedIdx->size());
	AK4UnmatchedIdx03->reserve( ak4UnmatchedIdx03->size());
//	AK4UnmatchedIdx10->reserve( ak4UnmatchedIdx10->size());
//	AK4UnmatchedIdx30->reserve( ak4UnmatchedIdx30->size());

	std::copy(subjet8CSVV1->begin(), subjet8CSVV1->end(),
              std::back_inserter(*sjCSVV1AK8));

	std::copy(subjet8CSV->begin(), subjet8CSV->end(),
              std::back_inserter(*sjCSVAK8));
	//cout << "copy"<< endl;
/*
	std::copy(ak4UnmatchedIdx->begin(), ak4UnmatchedIdx->end(),
              std::back_inserter(*AK4UnmatchedIdx));
*/
	std::copy(ak4UnmatchedIdx03->begin(), ak4UnmatchedIdx03->end(),
              std::back_inserter(*AK4UnmatchedIdx03));
/*
	std::copy(ak4UnmatchedIdx10->begin(), ak4UnmatchedIdx10->end(),
              std::back_inserter(*AK4UnmatchedIdx10));

	std::copy(ak4UnmatchedIdx30->begin(), ak4UnmatchedIdx30->end(),
              std::back_inserter(*AK4UnmatchedIdx30));
*/
	std::copy(hjetsIdx->begin(), hjetsIdx->end(),
              std::back_inserter(*idxHTag));

	std::copy(hjetsIdxSB0->begin(), hjetsIdxSB0->end(),
              std::back_inserter(*idxHTagSB0));

	std::copy(hjetsIdxSB1->begin(), hjetsIdxSB1->end(),
              std::back_inserter(*idxHTagSB1));

//	std::copy(tjetsIdx03sub->begin(), tjetsIdx03sub->end(),
//              std::back_inserter(*idxTTag03sub));

	std::copy(tjetsIdx03->begin(), tjetsIdx03->end(),
              std::back_inserter(*idxTTag03));

	std::copy(tjetsIdx03SB0->begin(), tjetsIdx03SB0->end(),
              std::back_inserter(*idxTTag03SB0));
/*
	std::copy(tjetsIdx10->begin(), tjetsIdx10->end(),
              std::back_inserter(*idxTTag10));

	std::copy(tjetsIdx30->begin(), tjetsIdx30->end(),
              std::back_inserter(*idxTTag30));

	std::copy(tjetsIdxsub->begin(), tjetsIdxsub->end(),
              std::back_inserter(*idxTTagsub));

	std::copy(tjetsIdxsub->begin(), tjetsIdxsub2->end(),
              std::back_inserter(*idxTTagsub2));

	std::copy(tjetsIdx->begin(), tjetsIdx->end(),
              std::back_inserter(*idxTTag));

	std::copy(tjetsIdx0->begin(), tjetsIdx0->end(),
              std::back_inserter(*idxTTag0));

	std::copy(tjetsIdx1->begin(), tjetsIdx1->end(),
              std::back_inserter(*idxTTag1));

	std::copy(tjetsIdx2->begin(), tjetsIdx2->end(),
              std::back_inserter(*idxTTag2));

	std::copy(tjetsIdx3->begin(), tjetsIdx3->end(),
              std::back_inserter(*idxTTag3));
*/
        std::copy(wjetsIdx->begin(), wjetsIdx->end(),
              std::back_inserter(*idxWTag));

        std::copy(EvtWeight_->begin(), EvtWeight_->end(),
              std::back_inserter(*EvtWeight));

        std::copy(bjetsIdx->begin(), bjetsIdx->end(),
              std::back_inserter(*idxbTag));

        std::copy(jet8good->begin(), jet8good->end(),
              std::back_inserter(*idxAK8));

        std::copy(jetgood->begin(), jetgood->end(),
              std::back_inserter(*idxAK4));

        //Add PU weight
   	if(!_isData) {
   		EvtWeight->push_back(PUcorr->GetBinContent(ipuNtrueInt+1));
   		EvtWeight->push_back(PUcorr->GetBinContent(ipuNtrueInt));
   		EvtWeight->push_back(PUcorr->GetBinContent(ipuNtrueInt+2));
   		EvtWeight->push_back(PUcorr->GetBinContent(inpv+1));
	}
   	else {
		EvtWeight->push_back(1);
		EvtWeight->push_back(1);
		EvtWeight->push_back(1);
		EvtWeight->push_back(1);
	}

        if(_isTTJets)
		EvtWeight->push_back(*TTBarWeight);
	else
		EvtWeight->push_back(1);
		
	//cout << "Btags" << endl;
	// AK4 BTags

        looseBTag = mediumBTag = tightBTag = 0;
        //
        for( unsigned ak4idx : *ak4UnmatchedIdx03) {
		if(bjetsIdx->end() != std::find(bjetsIdx->begin(), bjetsIdx->end(), ak4idx)) {
                           if((*jet4CSV)[ak4idx] > .97) { tightBTag++;}
                           if((*jet4CSV)[ak4idx] > .89) { mediumBTag++;}
                           if((*jet4CSV)[ak4idx] > .605) { looseBTag++;}
                }
        }


	//Rel Mass
        TLorentzVector J1, J2;

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

        softDropMassLeadAK8 = (*softDropMassAK8)[(*jet8good)[0]];
        trimmedMassLeadAK8 = (*trimmedMassAK8)[(*jet8good)[0]];

	//Mass of T' candidate
	
	if(jet8good->size() >= 2 && idxHTag->size() >0 && idxTTag03->size() > 0) {
 		TLorentzVector TCand, HCand;
		
		HCand.SetPtEtaPhiM((*jet8pt)[(*idxHTag)[0]],
                         (*jet8eta)[(*idxHTag)[0]],
                         (*jet8phi)[(*idxHTag)[0]],
                         (*jet8M)[(*idxHTag)[0]]);

                TCand.SetPtEtaPhiM((*jet8pt)[(*idxTTag03)[0]],
                         (*jet8eta)[(*idxTTag03)[0]],
                         (*jet8phi)[(*idxTTag03)[0]],
                         (*jet8M)[(*idxTTag03)[0]]);

		massTprime = (HCand + TCand).M();
	}


	fMaxEtaAK4 = 0;
        for( unsigned int i = 0 ; i < ak4UnmatchedIdx03->size() ; i++ )
        {

        	if(jet4eta){
			//cout << jeteta <<"  " << i << endl;
		   if( fabs((*jet4eta)[(*ak4UnmatchedIdx03)[i]]) > fMaxEtaAK4)
			fMaxEtaAK4 = fabs((*jet4eta)[(*ak4UnmatchedIdx03)[i]]);
		}
        }

//	cout << "Fill" <<endl;

	cutTree->Fill();
}


// ------------ method called once each job just before starting event loop  ------------
void 
TprimeAna::beginJob()
{

  TFile * pufile = new TFile("PUcorrection.root");
  PUcorr = (TH1D*) pufile->Get("pileup");

//  cout << "begin job";
  cutTree = fs->make<TTree>("cutTree","cut variables");

  cutTree->Branch("trimmedMassLeadAK8", &trimmedMassLeadAK8, "trimmedMassLeadAK8/D");

  cutTree->Branch("npv",&inpv, "npv/I");
  cutTree->Branch("puNtrueInt",&ipuNtrueInt, "puNtrueInt/I");

  ptAK4 = new std::vector<double>;
  ptAK8 = new std::vector<double>;
  etaAK8 = new std::vector<double>;
  etaAK4 = new std::vector<double>;
  phiAK8 = new std::vector<double>;
  phiAK4 = new std::vector<double>;
  MAK8 = new std::vector<double>;
  MAK4 = new std::vector<double>;
  SoftDropMassAK8 = new std::vector<double>;
  tau1AK8 = new std::vector<double>;
  tau2AK8 = new std::vector<double>;
  tau3AK8 = new std::vector<double>;

  //ak8s = new AK8Jets();

  subjAK8 = new std::vector<unsigned>;
  idxAK8 = new std::vector<unsigned>;
  idxAK4 = new std::vector<unsigned>;
//  AK4UnmatchedIdx = new std::vector<unsigned>;
  AK4UnmatchedIdx03 = new std::vector<unsigned>;
//  AK4UnmatchedIdx10 = new std::vector<unsigned>;
//  AK4UnmatchedIdx30 = new std::vector<unsigned>;

//  cutTree->Branch("ak8s", &ak8s);
  cutTree->Branch("nAK8", &nAK8, "nAK8/i");
  cutTree->Branch("ptAK4", &ptAK4); 
  cutTree->Branch("etaAK4", &etaAK4);
  cutTree->Branch("phiAK4", &phiAK4);
  cutTree->Branch("ptAK8", &ptAK8); 
  cutTree->Branch("etaAK8", &etaAK8);
  cutTree->Branch("phiAK8", &phiAK8);
  cutTree->Branch("MAK8", &MAK8);
  cutTree->Branch("MAK4", &MAK4);
  cutTree->Branch("SoftDropMassAK8", &SoftDropMassAK8);
  cutTree->Branch("PrunedMassAK8", &PrunedMassAK8);
  cutTree->Branch("tau1AK8", &tau1AK8);
  cutTree->Branch("tau2AK8", &tau2AK8);
  cutTree->Branch("tau3AK8", &tau3AK8);
  cutTree->Branch("AK4Idx", &idxAK4); 
  cutTree->Branch("AK8Idx", &idxAK8); 
//  cutTree->Branch("AK4UnmatchedIdx", &AK4UnmatchedIdx);
  cutTree->Branch("AK4UnmatchedIdx03", &AK4UnmatchedIdx03);
//  cutTree->Branch("AK4UnmatchedIdx10", &AK4UnmatchedIdx10);
//  cutTree->Branch("AK4UnmatchedIdx30", &AK4UnmatchedIdx30);

  cutTree->Branch("subjAK8", &subjAK8);

  sj0IdxAK8 = new std::vector<float>;
  sj1IdxAK8 = new std::vector<float>;
  sj2IdxAK8 = new std::vector<float>;
  sj3IdxAK8 = new std::vector<float>;
  sjCSVAK8 = new std::vector<float>;
  sjCSVV1AK8 = new std::vector<float>;

  cutTree->Branch("sj0IdxAK8",&sj0IdxAK8);
  cutTree->Branch("sj1IdxAK8",&sj1IdxAK8);
  cutTree->Branch("sj2IdxAK8",&sj2IdxAK8);
  cutTree->Branch("sj3IdxAK8",&sj3IdxAK8);

  cutTree->Branch("sjCSVAK8",&sjCSVAK8);
  cutTree->Branch("sjCSVV1AK8",&sjCSVV1AK8);



  EvtWeight = new std::vector<double>;

  cutTree->Branch("EvtWeight", &EvtWeight);

  idxHTag = new std::vector<unsigned>;
  idxHTagSB0 = new std::vector<unsigned>;
  idxHTagSB1 = new std::vector<unsigned>;
//  idxTTag = new std::vector<unsigned>;
//  idxTTagsub = new std::vector<unsigned>;
//  idxTTagsub2 = new std::vector<unsigned>;
//  idxTTag0 = new std::vector<unsigned>;
//  idxTTag1 = new std::vector<unsigned>;
//  idxTTag2 = new std::vector<unsigned>;
//  idxTTag3 = new std::vector<unsigned>;
  idxTTag03 = new std::vector<unsigned>;
  idxTTag03SB0 = new std::vector<unsigned>;
//  idxTTag03sub = new std::vector<unsigned>;
//  idxTTag10 = new std::vector<unsigned>;
//  idxTTag30 = new std::vector<unsigned>;
  idxWTag = new std::vector<unsigned>;
  idxbTag = new std::vector<unsigned>;

  cutTree->Branch("WTagIdx", &idxWTag);  
  cutTree->Branch("bTagIdx", &idxbTag);
  cutTree->Branch("HTagIdx", &idxHTag);
  cutTree->Branch("HTagIdxSB0", &idxHTagSB0);
  cutTree->Branch("HTagIdxSB1", &idxHTagSB1);
//  cutTree->Branch("TTagIdx", &idxTTag);
//  cutTree->Branch("TTagIdxsub", &idxTTagsub);
//  cutTree->Branch("TTagIdxsub2", &idxTTagsub2);
  cutTree->Branch("TTagIdx03", &idxTTag03);
  cutTree->Branch("TTagIdx03SB0", &idxTTag03SB0);
//  cutTree->Branch("TTagIdx03sub", &idxTTag03sub);
//  cutTree->Branch("TTagIdx10", &idxTTag10);
//  cutTree->Branch("TTagIdx30", &idxTTag30);
//  cutTree->Branch("TTagIdx0", &idxTTag0);
//  cutTree->Branch("TTagIdx1", &idxTTag1);
//  cutTree->Branch("TTagIdx2", &idxTTag2);
//  cutTree->Branch("TTagIdx3", &idxTTag3);

  cutTree->Branch("relM",&relM,"relM/D");
  cutTree->Branch("relpt",&relpt,"relpt/D");
  cutTree->Branch("fMaxEtaAK4",&fMaxEtaAK4, "fMaxEtaAK4/D");
  cutTree->Branch("htak4",&htak4, "htak4/D");

  cutTree->Branch("bTrigger",&bTrigger,"bTrigger/O");

  cutTree->Branch("looseBTag", &looseBTag, "looseBTag/i");
  cutTree->Branch("mediumBTag", &mediumBTag, "mediumBTag/i");
  cutTree->Branch("tightBTag", &tightBTag, "tightBTag/i");

 

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

  

}



// ------------ method called once each job just after ending the event loop  ------------
void 
TprimeAna::endJob() 

{
	//delete ak8s;

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
