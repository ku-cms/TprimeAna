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
#include <TLorentzVector.h>
#include <string>
#include <iostream>

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

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
      //
/*  
    
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
      edm::Handle<std::vector<float> > mh_jetAK4GetPartonY;
      edm::Handle<std::vector<float> > mh_jetAK4Phi;
      edm::Handle<std::vector<float> > mh_jetAK4E;
      edm::Handle<std::vector<float> > mh_jetAK4HadronFlavour;
      edm::Handle<std::vector<float> > mh_jetAK4CSV;

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

*/

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
TprimeAna::TprimeAna(const edm::ParameterSet& iConfig)

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
      edm::Handle<double> mh_htak8jets;

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

      edm::Handle<std::vector<float> > mh_subjetsCmsTopTagsubjetCSVV1;

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
      edm::Handle<unsigned> mh_ngoodBTaggedAK4Jets;
      edm::Handle<unsigned> mh_nWJets;
      edm::Handle<unsigned> mh_nHJets;
      edm::Handle<unsigned> mh_nTJets;
      edm::Handle<double> mh_maxetaak4;
      edm::Handle<double> mh_MassLeading2AK8;
      edm::Handle<double> mh_DeltaEtaLeading2AK8;
      edm::Handle<double> mh_pt1stAK8;
      edm::Handle<double> mh_pt2ndAK8;
      edm::Handle<double> mh_mass1stAK8;
      edm::Handle<double> mh_mass2ndAK8;

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

      iEvent.getByLabel("presel","ak4goodjets", mh_jetAK4Good);
      iEvent.getByLabel("presel", "htak4jets", mh_htak4jets);

      iEvent.getByLabel("presel","ngoodAK4Jets", mh_ngoodAK4Jets);
      iEvent.getByLabel("presel","ngoodAK8Jets", mh_ngoodAK8Jets);
      iEvent.getByLabel("presel","ngoodBTaggedAK4Jets", mh_ngoodBTaggedAK4Jets);
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

      iEvent.getByLabel("subjetsCmsTopTag", "subjetsCmsTopTagsubjetCSVV1", mh_subjetsCmsTopTagsubjetCSVV1);

      iEvent.getByLabel("genPart", "genPartPt", mh_genPartPt);
      iEvent.getByLabel("genPart", "genPartEta", mh_genPartEta);
      iEvent.getByLabel("genPart", "genPartPhi", mh_genPartPhi);
      iEvent.getByLabel("genPart", "genPartE", mh_genPartE);
      iEvent.getByLabel("genPart", "genPartID", mh_genPartID);
      iEvent.getByLabel("genPart", "genPartStatus", mh_genPartStatus);
      iEvent.getByLabel("genPart", "genPartMomID", mh_genPartMomID);
      iEvent.getByLabel("genPart", "genPartMom0ID", mh_genPartMom0ID);
      iEvent.getByLabel("genPart", "genPartMom1ID", mh_genPartMom1ID);
      iEvent.getByLabel("genPart", "genPartDau0ID", mh_genPartDau0ID);
      iEvent.getByLabel("genPart", "genPartDau1ID", mh_genPartDau1ID);

      const std::vector<float> * jetcsv = mh_jetAK4CSV.product();
      const std::vector<float> * jetpt = mh_jetAK4Pt.product();
      const std::vector<float> * jeteta = mh_jetAK4Eta.product();
      const std::vector<float> * jetphi = mh_jetAK4Phi.product();
      const std::vector<float> * jetM = mh_jetAK4Mass.product();
      const std::vector<float> * jetflavor = mh_jetAK4HadronFlavour.product();
      const std::vector<unsigned> * jetgood = mh_jetAK4Good.product();

      const std::vector<float> * jet8pt = mh_jetAK8Pt.product();
      const std::vector<float> * jet8eta = mh_jetAK8Eta.product();
      const std::vector<float> * jet8phi = mh_jetAK8Phi.product();
      const std::vector<float> * jet8M = mh_jetAK8Mass.product();
      const std::vector<unsigned> * jet8good = mh_jetAK8Good.product();
      const std::vector<float> * jetAK8nSubjets = mh_jetAK8nSubjets.product();

      const std::vector<float> * subjet8CSV = mh_subjetsCmsTopTagsubjetCSVV1.product();

      const std::vector<float> * genPartID = mh_genPartID.product();
      const std::vector<float> * genPartMomID = mh_genPartMomID.product();
      const std::vector<float> * genPartStatus= mh_genPartStatus.product();
      const std::vector<float> * genPartEta = mh_genPartEta.product();
      const std::vector<float> * genPartPhi = mh_genPartPhi.product();

      const double * htak4jets = mh_htak4jets.product();
      const double * htak8jets = mh_htak8jets.product();

      const unsigned * ngoodAK4Jets = mh_ngoodAK4Jets.product();
      const unsigned * ngoodAK8Jets = mh_ngoodAK8Jets.product();
      const unsigned * ngoodBTaggedAK4Jets = mh_ngoodBTaggedAK4Jets.product();
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
      const std::vector<float> * jetAK8Phi = mh_jetAK8Phi.product();
      const std::vector<float> * jetAK8Eta = mh_jetAK8Eta.product();
      const std::vector<float> * jetAK8Mass = mh_jetAK8Mass.product();

      const ULong64_t * evtNum = mh_evtNum.product();

      int idx1 = -1;
      int idx2 = -1; 

      float Ht = 0;

      int iBTags = 0;

      //for( unsigned int i = 0 ; i < jetpt->size() ; i++ )
      for( unsigned int i = 0 ; i < jetgood->size() ; i++ )
	{
	        
		histos["AK4JetPt"]->Fill((*jetpt)[(*jetgood)[i]]);
		if(jetcsv)
		  if( (*jetcsv)[(*jetgood)[i]] > 0.89 )
			iBTags++;

		Ht += (*jetpt)[(*jetgood)[i]];

		float fMindR = 99;

	//	for(unsigned int i = 0; i < jetpt->size() ; i++ ) {
		   for(unsigned int j = 0 ; j < jetgood->size() ; j++)
		   {
			if(i == j)
				continue;

			float dR = deltaR((*jeteta)[(*jetgood)[i]],(*jetphi)[(*jetgood)[i]],(*jeteta)[(*jetgood)[j]],(*jetphi)[(*jetgood)[j]]);

			histos["AK4JetdR"]->Fill(dR);

			if(dR < fMindR)
			{
			    idx1 = (*jetgood)[i];
			    idx2 = (*jetgood)[j];
			    fMindR = deltaR((*jeteta)[(*jetgood)[i]],(*jetphi)[(*jetgood)[i]],(*jeteta)[(*jetgood)[j]],(*jetphi)[(*jetgood)[j]]);
			}
		   }
		//}
	}	

	histos["AK4JetHt"]->Fill(Ht);
	histos["AK4Ht"]->Fill(*htak4jets);
	histos["AK8Ht"]->Fill(*htak8jets);

	histos["nTTags"]->Fill(*nTJets);
	histos["nWTags"]->Fill(*nWJets);
	histos["nHTags"]->Fill(*nHJets);

	histos["AK4Jets"]->Fill(jetgood->size());
	histos["AK4BTags"]->Fill(iBTags);

	histos["ngoodAK4Jets"]->Fill(*ngoodAK4Jets);
        histos["ngoodAK8Jets"]->Fill(*ngoodAK8Jets);
        histos["ngoodBTaggedAK4Jets"]->Fill(*ngoodBTaggedAK4Jets);
        histos["nWJets"]->Fill(*nWJets);
        histos["nHJets"]->Fill(*nHJets);
        histos["maxetaak4"]->Fill(*maxetaak4);
        histos["MassLeading2AK8"]->Fill(*MassLeading2AK8);
        histos["DeltaEtaLeading2AK8"]->Fill(*DeltaEtaLeading2AK8);
        histos["pt1stAK8"]->Fill(*pt1stAK8);
        histos["pt2ndAK8"]->Fill(*pt2ndAK8);
        histos["mass1stAK8"]->Fill(*mass1stAK8);
        histos["mass2ndAK8"]->Fill(*mass2ndAK8);

	// Rel pt
	
	float relpt = (*pt1stAK8 + *pt2ndAK8) / Ht;

	histos["relpt"]->Fill(relpt);

	int tidx = -1;
	int h1idx = -1;
	int h2idx = -1;

	for(unsigned int i = 0 ; i < genPartID->size() ; i++)
	{

	   if((*genPartID)[i] == 5)
	   {
		if((*genPartMomID)[i] == 6)
		{
	    	   tidx = i;	
		}	
		if((*genPartMomID)[i] == 25 && h1idx == -1)
		{
		   h1idx = i;	
		} else if ((*genPartMomID)[i] == 25)
		  {	
			h2idx = i;
		  }
	   }

	}
	
	histos["drHiggs"]->Fill(deltaR((*genPartEta)[h1idx],(*genPartPhi)[h1idx],(*genPartEta)[h2idx],(*genPartPhi)[h2idx]));

	bool bh1,bh2,bt;
	bh1=bh2=bt=false;	

	for(unsigned int i = 0 ; i < jeteta->size() ; i++)
	{
	    if(deltaR((*genPartEta)[tidx],(*genPartPhi)[tidx],(*jeteta)[i],(*jetphi)[i]) < 0.5)
	    {
		bt = true;
	    }	
	    if(deltaR((*genPartEta)[h1idx],(*genPartPhi)[h1idx],(*jeteta)[i],(*jetphi)[i]) < 0.5)
	    {
		bh1 = true;
	    }		
	    if(deltaR((*genPartEta)[h2idx],(*genPartPhi)[h2idx],(*jeteta)[i],(*jetphi)[i]) < 0.5)
	    {
		bh2 = true;
	    }		
	}
	if(bt)
		histos["ak4tMatched"]->Fill(1);
	
	if(bh1 && bh2)
		histos["ak4hMatched"]->Fill(2);
	else if(bh1 || bh2)
		histos["ak4hMatched"]->Fill(1);

	bh1=bh2=bt=false;	

	
        tidx = -1;
        h1idx = -1;
        h2idx = -1;

        for(unsigned int i = 0 ; i < genPartID->size() ; i++)
        {

                if((*genPartID)[i] == 6)
                {
                   tidx = i;
                }
                if((*genPartID)[i] == 25)
                {
                   h1idx = i;
                } 
        }

	for(unsigned int i = 0 ; i < jetAK8Eta->size() ; i++)
	{

	    if(deltaR((*genPartEta)[tidx],(*genPartPhi)[tidx],(*jetAK8Eta)[i],(*jetAK8Phi)[i]) < 0.5)
            {
                bt = true;
		histos["ak8tMatchedMass"]->Fill((*jetAK8Mass)[i]);
            }
            if(deltaR((*genPartEta)[h1idx],(*genPartPhi)[h1idx],(*jetAK8Eta)[i],(*jetAK8Phi)[i]) < 0.5)
            {
                bh1 = true;
		histos["ak8hMatchedMass"]->Fill((*jetAK8Mass)[i]);
            }
        }
	  
        if(bt)
		histos["ak8tMatched"]->Fill(1);

	if(bh1)	
		histos["ak8hMatched"]->Fill(1);		

//	histos["ak4hMatched"]->Fill(

//	histos["ak8tMatched"]->Fill
//	histos["ak8hMatched"]
	

	
	


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

	//Selection
	//
	
//	cout << "CSV size: " <<  subjet8CSV->size() << endl;
//	cout << "jetAK8nSubjets size: " << jetAK8nSubjets->size() << endl;

	bool bcsv[2];
	bcsv[0] = false;
	bcsv[1] = false;

	if(jet8good->size() == 2)
	{
	
	    unsigned subjetindex = 0;
	    for( unsigned k = 0 ; k < jet8good->size() ; k++) {
//		cout << "good jet at index: " << (*jet8good)[k] << endl;
	      for( unsigned j = 0 ; j < (*jet8good)[k] ; j++) {
//	 	cout << "jet at index "<< j << " has " <<(*jetAK8nSubjets)[j] << " subjets "  << endl;
		subjetindex += (*jetAK8nSubjets)[j];
		
	      }
//	      cout << "subjet index for jet " <<  k<<" : " << subjetindex << endl;
	      int btags = 0; 
	      string sb("nBTags");
	      for ( unsigned i = subjetindex ; i < subjetindex + (*jetAK8nSubjets)[(*jet8good)[k]] ; i++ ) {
//		cout << (*subjet8CSV)[i] << endl;
		if( (*subjet8CSV)[i] > 0.814 ){
			bcsv[k] = true;
			btags++;
		}
	      }
		histos[ sb + to_string(k+1) ]->Fill(btags);
	    }
	}

	bool bTwobs = (bcsv[0] && bcsv[1]);

//	cout << "2bs" << bTwobs << endl;

	bool bDeltaEtaLeading2AK8 = (*DeltaEtaLeading2AK8 < 2);
	
	// 2 AK8 Jets
	bool b2AK8Jets = (*ngoodAK8Jets == 2);

	// TMass	
	bool bTMass = (( *mass1stAK8 > 160 && *mass1stAK8 < 190) || (*mass2ndAK8 > 160 && *mass2ndAK8 < 190));
		
	
	//HMass
	bool bHMass = (( *mass1stAK8 > 110 && *mass1stAK8 < 140) || (*mass2ndAK8 > 110 && *mass2ndAK8 < 140));

	// H Tag
	bool bHTag = (*nHJets == 1);

	// T Tag
	bool bTTag = (*nTJets == 1);


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

	bool brelM = (relM > 0.15 && relM < 0.3);
	
	bool bForwardJet = false;
        for( unsigned int i = 0 ; i < jetgood->size() ; i++ )
        {

                if(jeteta)
                  if( fabs((*jeteta)[(*jetgood)[i]]) > 1.5 )
                        bForwardJet = true;
	}

	bool isHbb = false;

	int numBs = 0;

	for( unsigned int i = 0 ; i < genPartID->size() ; i++ )
	{
	
	    if ( fabs((*genPartID)[i]) == 5 && fabs((*genPartMomID)[i]) == 25)
		numBs++;

	}
	isHbb = (numBs == 2);

	if( isHbb && bTwobs) // Hbb
		histos[ "Selection" ]->Fill(0) ; 
	if( isHbb && b2AK8Jets ) 
		histos[ "Selection" ]->Fill(1) ; 
	if( isHbb && b2AK8Jets && bTMass) 
		histos[ "Selection" ]->Fill(2) ; 
	if( isHbb && b2AK8Jets && bHMass)
		histos[ "Selection" ]->Fill(3) ; 
	if( isHbb && b2AK8Jets && bTMass && bHMass) 
		histos[ "Selection" ]->Fill(4) ; 
	if( isHbb && b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8) 
		histos[ "Selection" ]->Fill(5) ; 
	if( isHbb && b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8 && bForwardJet) // Hbb
		histos[ "Selection" ]->Fill(6) ;
	if( isHbb && b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8 && bForwardJet && brelpt)
		histos[ "Selection" ]->Fill(7) ;
	if( isHbb && b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8 && bForwardJet && brelpt && brelM)
		histos[ "Selection" ]->Fill(8) ;
 
	if( !isHbb)
		histos[ "Selection" ]->Fill(9) ; 
	if( !isHbb && b2AK8Jets )
                histos[ "Selection" ]->Fill(10) ;
        if( !isHbb && b2AK8Jets && bTMass) 
                histos[ "Selection" ]->Fill(11) ;
        if( !isHbb && b2AK8Jets && bHMass)
                histos[ "Selection" ]->Fill(12) ;
        if( !isHbb && b2AK8Jets && bTMass && bHMass)
                histos[ "Selection" ]->Fill(13) ;
        if( !isHbb && b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8)
                histos[ "Selection" ]->Fill(14) ;
        if( !isHbb && b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8 && bForwardJet) // Hbb
                histos[ "Selection" ]->Fill(15) ;
        if( !isHbb && b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8 && bForwardJet && brelpt) // Hbb
                histos[ "Selection" ]->Fill(16) ;
        if( !isHbb && b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8 && bForwardJet && brelpt && brelM) // Hbb
                histos[ "Selection" ]->Fill(17) ;
		
        histos[ "Selection" ]->Fill(18) ;
        if( b2AK8Jets )
                histos[ "Selection" ]->Fill(19) ;
        if( b2AK8Jets && bTMass)
                histos[ "Selection" ]->Fill(20) ;
        if( b2AK8Jets && bHMass)
                histos[ "Selection" ]->Fill(21) ;
        if( b2AK8Jets && bTMass && bHMass)
                histos[ "Selection" ]->Fill(22) ;
        if( b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8)
                histos[ "Selection" ]->Fill(23) ;
        if( b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8 && bForwardJet) // Hbb
                histos[ "Selection" ]->Fill(24) ;
        if( b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8 && bForwardJet && brelpt) // Hbb
                histos[ "Selection" ]->Fill(25) ;
        if( b2AK8Jets && bTMass && bHMass && bDeltaEtaLeading2AK8 && bForwardJet && brelpt && brelM) // Hbb
                histos[ "Selection" ]->Fill(26) ;


        if( isHbb ) // Hbb
                histos[ "Selection2" ]->Fill(0) ;
        if( isHbb && b2AK8Jets )
                histos[ "Selection2" ]->Fill(1) ;
        if( isHbb && b2AK8Jets && bTTag)
                histos[ "Selection2" ]->Fill(2) ;
        if( isHbb && b2AK8Jets && bHTag)
                histos[ "Selection2" ]->Fill(3) ;
        if( isHbb && b2AK8Jets && bTTag && bHTag)
                histos[ "Selection2" ]->Fill(4) ;
        if( isHbb && b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8)
                histos[ "Selection2" ]->Fill(5) ;
        if( isHbb && b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8 && bForwardJet) // Hbb
                histos[ "Selection2" ]->Fill(6) ;
	if( isHbb && b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8 && bForwardJet && brelpt)
		histos[ "Selection2" ]->Fill(7) ;
	if( isHbb && b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8 && bForwardJet && brelpt && brelM)
		histos[ "Selection2" ]->Fill(8) ;
        if( !isHbb)
                histos[ "Selection2" ]->Fill(9) ;
        if( !isHbb && b2AK8Jets )
                histos[ "Selection2" ]->Fill(10) ;
        if( !isHbb && b2AK8Jets && bTTag)
                histos[ "Selection2" ]->Fill(11) ;
        if( !isHbb && b2AK8Jets && bHTag)
                histos[ "Selection2" ]->Fill(12) ;
        if( !isHbb && b2AK8Jets && bTTag && bHTag)
                histos[ "Selection2" ]->Fill(13) ;
        if( !isHbb && b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8)
                histos[ "Selection2" ]->Fill(14) ;
        if( !isHbb && b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8 && bForwardJet) // Hbb
                histos[ "Selection2" ]->Fill(15) ;
        if( !isHbb && b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8 && bForwardJet && brelpt) // Hbb
                histos[ "Selection2" ]->Fill(16) ;
        if( !isHbb && b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8 && bForwardJet && brelpt && brelM) // Hbb
                histos[ "Selection2" ]->Fill(17) ;

        histos[ "Selection2" ]->Fill(18) ;
        if( b2AK8Jets )
                histos[ "Selection2" ]->Fill(19) ;
        if( b2AK8Jets && bTTag)
                histos[ "Selection2" ]->Fill(20) ;
        if( b2AK8Jets && bHTag)
                histos[ "Selection2" ]->Fill(21) ;
        if( b2AK8Jets && bTTag && bHTag)
                histos[ "Selection2" ]->Fill(22) ;
        if( b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8)
                histos[ "Selection2" ]->Fill(23) ;
        if( b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8 && bForwardJet) // Hbb
                histos[ "Selection2" ]->Fill(24) ;
        if( b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8 && bForwardJet && brelpt) // Hbb
                histos[ "Selection2" ]->Fill(25) ;
        if( b2AK8Jets && bTTag && bHTag && bDeltaEtaLeading2AK8 && bForwardJet && brelpt && brelM) // Hbb
                histos[ "Selection2" ]->Fill(26) ;


	 if( b2AK8Jets && bTTag && bHTag)
                histos[ "SidebandD" ]->Fill(*MassLeading2AK8) ;
	 if( b2AK8Jets && !bTTag && !bHTag)
                histos[ "SidebandA" ]->Fill(*MassLeading2AK8) ;
	 if( b2AK8Jets && bTTag && !bHTag)
                histos[ "SidebandC" ]->Fill(*MassLeading2AK8) ;
	 if( b2AK8Jets && !bTTag && bHTag)
                histos[ "SidebandB" ]->Fill(*MassLeading2AK8) ;

}


// ------------ method called once each job just before starting event loop  ------------
void 
TprimeAna::beginJob()
{
  histos[ "nBTags1" ] = fs->make<TH1F>( "nBTags1", "# of subjet BTags in jet 1" , 5, 0, 5);
  histos[ "nBTags2" ] = fs->make<TH1F>( "nBTags2", "# of subjet BTags in jet 2" , 5, 0, 5);

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
  histos[ "AK8Ht" ] = fs->make<TH1F>( "AK8 Ht"  , "H_{t}", 1000,  0., 2000. );
  histos[ "AK4JetdR" ] = fs->make<TH1F>( "jetdR" , "dR between Jets", 50, 0. ,5.);
  histos[ "AK4JetPairMass" ] = fs->make<TH1F>( "jetPairMass"  , "Jet Pair Mass", 500,  0., 1000. );
  histos[ "AK4JetFlavor" ] = fs->make<TH1F>( "jetPairFlavor"  , "Jet Pair Flavor", 10,  0., 10. );
  histos[ "AK4BTags" ] = fs->make<TH1F>( "jetBTags"  , "Jet BTags", 10,  0., 10. );
  histos[ "AK4Jets" ] = fs->make<TH1F>( "jets"  , "Jets after sel", 10,  0., 10. );

  histos[ "ngoodAK4Jets" ] = fs->make<TH1F>( "ngoodAK4Jets"  , "AK4 Jets after sel", 20,  0., 20. );
 histos[ "ngoodAK8Jets" ] = fs->make<TH1F>( "ngoodAK8Jets"  , "AK8 Jets after sel", 20,  0., 20. );
 histos[ "ngoodBTaggedAK4Jets" ] = fs->make<TH1F>( "ngoodBTaggedAK4Jets"  , "Jets after sel", 10,  0., 10.  );
 histos[ "nWJets" ] = fs->make<TH1F>("nWJets"  , "nWJets", 10,  0., 10. );
 histos[ "nHJets" ] = fs->make<TH1F>("nHJets"  , "nHJets", 10,  0., 10. );
 histos[ "maxetaak4" ]= fs->make<TH1F>("maxetaak4","maxetaak4",50, 0. ,5. );
 histos[ "MassLeading2AK8" ]= fs->make<TH1F>( "MassLeading2AK8","MassLeading2AK8",500,  0., 1000.);
 histos[ "DeltaEtaLeading2AK8" ]= fs->make<TH1F>("deltaetaak8","delta eta ak8 ", 100, 0 ,10);
 histos[ "pt1stAK8" ]= fs->make<TH1F>("pt1stAK8","pt1stAK8", 500,  0., 1000.);
 histos[ "pt2ndAK8" ]= fs->make<TH1F>("pt2ndAK8","pt2ndAK8", 500,  0., 1000.);
 histos[ "mass1stAK8" ]= fs->make<TH1F>( "mass1stAK8","mass1stAK8",500,  0., 1000.);
 histos[ "mass2ndAK8" ]= fs->make<TH1F>( "mass2ndAK8","mass2ndAK8",500,  0., 1000.);

 histos[ "ak4tMatched" ]= fs->make<TH1F>( "ak4tMatched","ak4tMatched",3,0,3);
 histos[ "ak4hMatched" ]= fs->make<TH1F>( "ak4hMatched","ak4hMatched",3,0,3);
 histos[ "ak8tMatched" ]= fs->make<TH1F>( "ak8tMatched","ak8tMatched",3,0,3);
 histos[ "ak8hMatched" ]= fs->make<TH1F>( "ak8hMatched","ak8hMatched",3,0,3);
 
 histos[ "ak8tMatchedMass" ]= fs->make<TH1F>( "ak8tMatchedMass","ak8tMatchedMass",300,0,300);
 histos[ "ak8hMatchedMass" ]= fs->make<TH1F>( "ak8hMatchedMass","ak8hMatchedMass",300,0,300);

 //histos[ "drHiggs" ] = fs->make<TH1F>( "drHiggs","drHiggs",

 histos[ "SidebandA" ]= fs->make<TH1F>( "SidebandA","SidebandA" ,500,  0., 1000.);
 histos[ "SidebandB" ]= fs->make<TH1F>( "SidebandB","SidebandB" ,500,  0., 1000.);
 histos[ "SidebandC" ]= fs->make<TH1F>( "SidebandC","SidebandC" ,500,  0., 1000.);
 histos[ "SidebandD" ]= fs->make<TH1F>( "SidebandD","SidebandD" ,500,  0., 1000.);

 histos[ "DEstimate" ]= fs->make<TH1F>( "DEstimate","DEstimate" ,500,  0., 1000.);

}



// ------------ method called once each job just after ending the event loop  ------------
void 
TprimeAna::endJob() 

{

	for( unsigned int i = 1; i < 500; i++ )
	{
		int A = histos[ "SidebandA" ]->GetBinContent(i);
		int B = histos[ "SidebandB" ]->GetBinContent(i);
		int C = histos[ "SidebandC" ]->GetBinContent(i);
		histos[ "DEstimate" ]->SetBinContent(i,B*C/A);


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
