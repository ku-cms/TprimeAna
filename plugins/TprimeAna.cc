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

      edm::Handle<std::vector<float> > mh_subjetCmsTopTagCSVV1;
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


      iEvent.getByLabel("jetsAK8", "jetAK8Pt", mh_jetAK8Pt);
      iEvent.getByLabel("jetsAK8", "jetAK8Eta", mh_jetAK8Eta);
      iEvent.getByLabel("jetsAK8", "jetAK8Phi", mh_jetAK8Phi);
      iEvent.getByLabel("jetsAK8", "jetAK8E", mh_jetAK8E);
      iEvent.getByLabel("jetsAK8", "jetAK8Mass", mh_jetAK8Mass);
      iEvent.getByLabel("jetsAK8", "jetAK8subjetIndex0", mh_jetAK8subjetIndex0);
      iEvent.getByLabel("jetsAK8", "jetAK8subjetIndex1", mh_jetAK8subjetIndex1);
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

      iEvent.getByLabel("subjetsCmsTopTag", "subjetCmsTopTagCSVV1", mh_subjetCmsTopTagCSVV1);

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

      const std::vector<float> * jet8pt = mh_jetAK8Pt.product();
      const std::vector<float> * jet8eta = mh_jetAK8Eta.product();
      const std::vector<float> * jet8phi = mh_jetAK8Phi.product();
      const std::vector<float> * jet8M = mh_jetAK8Mass.product();
      const std::vector<unsigned> * jet8good = mh_jetAK8Good.product();
      const std::vector<float> * softDropMassAK8 = mh_jetAK8SoftDropMass.product();
      const std::vector<float> * trimmedMassAK8 = mh_jetAK8TrimmedMass.product();

      const unsigned * nAK4Unmatched = mh_nAk4Unmatched.product();
      const std::vector<unsigned> * tjetsIdx_lsubj = mh_tjetsIdx_lsubj.product();
      const std::vector<unsigned> * hjetsIdx_lsubj = mh_hjetsIdx_lsubj.product();
      const std::vector<unsigned> * bjetsIdx = mh_bjetsIdx.product();

//      const std::vector<float> * jetAK8nSubjets = mh_jetAK8nSubjets.product();

//      const std::vector<float> * subjet8CSV = mh_subjetCmsTopTagCSVV1.product();
/*
      const std::vector<float> * genPartID = mh_genPartID.product();
      const std::vector<float> * genPartMomID = mh_genPartMom0ID.product();
      const std::vector<float> * genPartStatus= mh_genPartStatus.product();
      const std::vector<float> * genPartEta = mh_genPartEta.product();
      const std::vector<float> * genPartPhi = mh_genPartPhi.product();
*/
      const double * htak4jets = mh_htak4jets.product();
      const double * htak4trigjets = mh_htak4trigjets.product();
      const double * htak8jets = mh_htak8jets.product();

      const std::vector<unsigned> * ak4UnmatchedIdx = mh_ak4UnmatchedIdx.product(); 
     

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



//	Trigger
//
 if(_isData){
  unsigned int hltdecisions(0) ;
  for ( unsigned int i = 0 ; i < h_trigName.product()->size() ; i++ ) {
    //vector<string>::const_iterator it = find( (h_trigName.product())->begin(), (h_trigName.product())->end(), myhltpath) ; 

        //Support regex pattern matching: wildcards . and .*
        //
       bool bPass = 0;
       for( const string &myhltpath : hltPaths_ ) {

           string hltname = h_trigName.product()->at(i);
           boost::regex pattern(myhltpath);


                                      //      cout << hltname << "  " << pattern << "  " << result << endl;

           bPass |= boost::regex_match(hltname , pattern);
           hltdecisions += (pow(2,i) && bPass);
       }
   }
   if (hltdecisions == 0) return;
 }
 else {
	if (*htak4trigjets < 800) return;
	
 }


    //  if(*nAk4Unmatched < 4) return;

      int idx1 = -1;
      int idx2 = -1; 

      float Ht = 0;

//      int iBTags = 0;

//     cout << "Evt: " << evtNum << endl;
//	cout << "histos1" << endl;	



	histos["AK4Ht"]->Fill(*htak4jets);
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

	// dPhi 2 AK8
	//
	bool bdPhiAK8 = false;
	if(jet8good->size() > 1) {

		float dPhiLeadingAK8 = deltaPhi((*jet8phi)[(*jet8good)[0]],(*jet8phi)[(*jet8good)[1]]);

		histos["dPhiLeadingAK8"]->Fill (dPhiLeadingAK8);
		bdPhiAK8 = ( dPhiLeadingAK8 > 2);

		histos["eta1stAK8"]->Fill( (*jet8eta)[(*jet8good)[0]]);
		histos["eta2ndAK8"]->Fill( (*jet8eta)[(*jet8good)[1]]);
	}
	// Rel pt
	
	float relpt = (*pt1stAK8 + *pt2ndAK8) / Ht;

	histos["relpt"]->Fill(relpt);



// 	cout << "Jet Pair" << endl;
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




	
	// 2 AK8 Jets
	bool b2AK8Jets = (*ngoodAK8Jets > 1);

	// 6+ AK4 Jets
//	bool b6AK4Jets = (*ngoodAK4Jets > 5 );
	bool b2AK4Jets = (*nAK4Unmatched > 1 );
	bool b1AK4Jets = (*nAK4Unmatched > 0 );

	// TMass	
//	bool bTMass = (( *mass1stAK8 > 160 && *mass1stAK8 < 190) || (*mass2ndAK8 > 160 && *mass2ndAK8 < 190));
		
	
	//HMass
//	bool bHMass = (( *mass1stAK8 > 110 && *mass1stAK8 < 140) || (*mass2ndAK8 > 110 && *mass2ndAK8 < 140));

	// H Tag
	bool bHTag = (hjetsIdx_lsubj->size() > 0);

	// T Tag
	bool bTTag = (tjetsIdx_lsubj->size() > 0);

	//cout << "H T Tag" << endl;
	// b-tagged jets
	
	unsigned looseBTag, mediumBTag, tightBTag;
	looseBTag = mediumBTag = tightBTag = 0;

	for( unsigned ak4idx : *ak4UnmatchedIdx) {
		if(bjetsIdx->end() != std::find(bjetsIdx->begin(), bjetsIdx->end(), ak4idx)) {
	 	    if((*jetCSV)[ak4idx] > .97) { tightBTag++; continue;} 
	 	    if((*jetCSV)[ak4idx] > .89) { mediumBTag++; continue;} 
	 	    if((*jetCSV)[ak4idx] > .423) { looseBTag++; continue;} 
	        }
	}

	histos["AK4BTags-l"]->Fill(looseBTag);
	histos["AK4BTags-m"]->Fill(mediumBTag);
	histos["AK4BTags-t"]->Fill(tightBTag);

	//cout << "BTag " <<endl; 

	bool bLoose1 = (looseBTag > 0);
//	bool bLoose2 = (looseBTag > 1);

	bool bMedium1 = (mediumBTag > 0);
//	bool bMedium2 = (mediumBTag > 1);

	bool bTight1 = (tightBTag > 0);
//	bool bTight2 = (tightBTag > 1);

	
	// Rel Pt
	bool brelpt = (relpt > 0.65);

	// Rel M
	
	float relM = 0;
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

		histos[ "relM" ]->Fill(relM); 
	}
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
	double softDropMassLeadAK8 = (*softDropMassAK8)[(*jet8good)[0]];
	double trimmedMassLeadAK8 = (*trimmedMassAK8)[(*jet8good)[0]];
	double ptLeadingAK4,pt2ndAK4,pt3rdAK4,pt4thAK4,pt5thAK4,pt6thAK4;

	ptLeadingAK4=pt2ndAK4=pt3rdAK4=pt4thAK4=pt5thAK4=pt6thAK4 = 0;


	if(ak4UnmatchedIdx->size() >0 ){
		ptLeadingAK4 = (*jetpt)[(*ak4UnmatchedIdx)[0]]; 
		histos["ptLeadingAK4"]->Fill(ptLeadingAK4);
		histos["etaLeadingAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[0]]);
	}

	if(ak4UnmatchedIdx->size() >1 ){
		pt2ndAK4 = (*jetpt)[(*ak4UnmatchedIdx)[1]]; 
		histos["pt2ndAK4"]->Fill(pt2ndAK4);
		histos["eta2ndAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[1]]);
	}
	if(ak4UnmatchedIdx->size() >2 ){
		pt3rdAK4 = (*jetpt)[(*ak4UnmatchedIdx)[2]]; 
		histos["pt3rdAK4"]->Fill(pt3rdAK4);
		histos["eta3rdAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[2]]);
	}
	if(ak4UnmatchedIdx->size() >3 ){
		pt4thAK4 = (*jetpt)[(*ak4UnmatchedIdx)[3]]; 
		histos["pt4thAK4"]->Fill(pt4thAK4);
		histos["eta4thAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[3]]);
	}
	if(ak4UnmatchedIdx->size() > 4 ){
		pt5thAK4 = (*jetpt)[(*ak4UnmatchedIdx)[4]]; 
		histos["pt5thAK4"]->Fill(pt5thAK4);
		histos["eta5thAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[4]]);
	}
	if(ak4UnmatchedIdx->size() >5 ){
		pt6thAK4 = (*jetpt)[(*ak4UnmatchedIdx)[5]]; 
		histos["pt6thAK4"]->Fill(pt6thAK4);
		histos["eta6thAK4"]->Fill((*jeteta)[(*ak4UnmatchedIdx)[5]]);
	}

	bool bAK4LeadingPt = (ptLeadingAK4 < 200 );
	bool bMass2AK8 = ( *MassLeading2AK8 > 950 and *MassLeading2AK8 < 1400  );
	bool bSoftDropMassAK8 = (softDropMassLeadAK8 > 60);
	bool bTrimmedMassAK8 = ( trimmedMassLeadAK8 > 60);

// 	histos["2AK4Mass"]->Fill(mass2AK4);
	histos["softDropMassAK8"]->Fill(softDropMassLeadAK8);
	histos["trimmedMassAK8"]->Fill(trimmedMassLeadAK8);

	//cout << " histos x " << endl;

//  h1_["trimmedmak8leading"] -> Fill((goodAK8Jets.at(0)).getTrimmedMass()) ;
//  h1_["softdropmak8leading"] -> Fill((goodAK8Jets.at(0)).getSoftDropMass()) ;

	bool brelM = (relM > 0.15 && relM < 0.35);
	
	bool bForwardJet = false;
        for( unsigned int i = 0 ; i < ak4UnmatchedIdx->size() ; i++ )
        {

                if(jeteta)
                  if( fabs((*jeteta)[(*ak4UnmatchedIdx)[i]]) > 1.5 )
                        bForwardJet = true;
	}


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
	if( b2AK8Jets && bMass2AK8) 
		histos[ "Selection" ]->Fill(16) ; 
	if( b2AK8Jets && bTight1 && bHTag && bTTag && brelM && bSoftDropMassAK8 && bMass2AK8) 
		histos[ "Selection" ]->Fill(17) ; 
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
}


// ------------ method called once each job just before starting event loop  ------------
void 
TprimeAna::beginJob()
{

//  cout << "begin job";


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
  histos[ "AK4Ht" ] = fs->make<TH1F>( "AK4 Ht"  , "H_{t}", 1000,  0., 2000. );
  histos[ "AK4trigHt" ] = fs->make<TH1F>( "AK4 Ht"  , "H_{t}", 1000,  0., 2000. );
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
  histos[ "Selection" ]->GetXaxis()->SetBinLabel(17,"b2AK8Jets && bMass2AK8");

  histos[ "Selection" ]->GetXaxis()->SetBinLabel(18,"b2AK8Jets && bTight1 && bdPhiAK8 && bHTag && bTTag && brelM && bSoftDropMassAK8 && bMass2AK8");


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
