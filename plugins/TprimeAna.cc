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

      iEvent.getByLabel("jetsAK8", "jetAK8Pt", mh_jetAK8Pt);
      iEvent.getByLabel("jetsAK8", "jetAK8Eta", mh_jetAK8Eta);
      iEvent.getByLabel("jetsAK8", "jetAK8Phi", mh_jetAK8Phi);
      iEvent.getByLabel("jetsAK8", "jetAK8E", mh_jetAK8E);
      iEvent.getByLabel("jetsAK8", "jetAK8Mass", mh_jetAK8Mass);
      iEvent.getByLabel("jetsAK8", "jetAK8subjetIndex0", mh_jetAK8subjetIndex0);
      iEvent.getByLabel("jetsAK8", "jetAK8subjetIndex1", mh_jetAK8subjetIndex1);
      iEvent.getByLabel("jetsAK8", "jetAK8HadronFlavour", mh_jetAK8HadronFlavour);
      iEvent.getByLabel("jetsAK8", "jetAK8tau1", mh_jetAK8tau1);
      iEvent.getByLabel("jetsAK8", "jetAK8tau2", mh_jetAK8tau2);
      iEvent.getByLabel("jetsAK8", "jetAK8tau3", mh_jetAK8tau3);
      iEvent.getByLabel("presel", "ak8goodjets", mh_jetAK8Good);

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

      const std::vector<float> * genPartID = mh_genPartID.product();
      const std::vector<float> * genPartMomID = mh_genPartMomID.product();
      const std::vector<float> * genPartStatus= mh_genPartStatus.product();

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
	histos["AK4Jets"]->Fill(jetgood->size());
	histos["AK4BTags"]->Fill(iBTags);

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
	
	if( *evtNum < 10)
		for(unsigned int i = 0 ; i < genPartID->size(); i++)
		{

			std::cout << i << ":  " << (*genPartID)[i] << "      " << (*genPartMomID)[i] << "       " << (*genPartStatus)[i] << std::endl;

		}
}


// ------------ method called once each job just before starting event loop  ------------
void 
TprimeAna::beginJob()
{

  histos[ "AK4JetPt" ] = fs->make<TH1F>( "pt"  , "p_{t}", 500,  0., 1000. );
  histos[ "AK4JetHt" ] = fs->make<TH1F>( "Ht"  , "H_{t}", 1000,  0., 2000. );
  histos[ "AK4JetdR" ] = fs->make<TH1F>( "jetdR" , "dR between Jets", 50, 0. ,5.);
  histos[ "AK4JetPairMass" ] = fs->make<TH1F>( "jetPairMass"  , "Jet Pair Mass", 500,  0., 1000. );
  histos[ "AK4JetFlavor" ] = fs->make<TH1F>( "jetPairFlavor"  , "Jet Pair Flavor", 10,  0., 10. );
  histos[ "AK4BTags" ] = fs->make<TH1F>( "jetBTags"  , "Jet BTags", 10,  0., 10. );
  histos[ "AK4Jets" ] = fs->make<TH1F>( "jets"  , "Jets after sel", 10,  0., 10. );
}

// ------------ method called once each job just after ending the event loop  ------------
void 
TprimeAna::endJob() 
{
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
