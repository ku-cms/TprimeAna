void SignalHT()
{
makeStack("ht", "isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"WtTrig(ht)*EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)" );

TFile f1("SignalHT-Nominal.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f1.Close();

makeStack("ht", "lhewts.first==3&&isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"WtTrig(ht)*EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)*lhewts.second" );

TFile f1a("SignalHT-Wgt2.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f1a.Close();

makeStack("ht", "lhewts.first==3&&isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"WtTrig(ht)*EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)*lhewts.second" );

TFile f1b("SignalHT-Wgt3.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f1b.Close();

makeStack("ht", "lhewts.first==4&&isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"WtTrig(ht)*EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)*lhewts.second" );

TFile f1c("SignalHT-Wgt4.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f1c.Close();


makeStack("ht", "lhewts.first==7&&isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"WtTrig(ht)*EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)*lhewts.second" );

TFile f1d("SignalHT-Wgt7.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f1d.Close();





/*
makeStack("ht", "isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*EvtWtHTUp*btagsf*topSF(ptTopTagged)" );

TFile f2("SignalHT-HTUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f2.Close();

makeStack("ht", "isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"WtTrig(ht)*EvtWeight*EvtWtPV*EvtWtHTDown*btagsf*topSF(ptTopTagged)" );

TFile f3("SignalHT-HTDown.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f3.Close();
*/

makeStack("ht", "isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf_lUp*topSF(ptTopTagged)" );

TFile f4("SignalHT-btag_lUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f4.Close();

makeStack("ht", "isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf_lDown*topSF(ptTopTagged)" );

TFile f5("SignalHT-btag_lDown.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f5.Close();

makeStack("ht", "isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf_bcUp*topSF(ptTopTagged)" );

TFile f6("SignalHT-btag_bcUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f6.Close();

makeStack("ht", "isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf_bcDown*topSF(ptTopTagged)" );

TFile f7("SignalHT-btag_bcDown.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f7.Close();

makeStack("ht", "isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf*topSFUp(ptTopTagged)" );

TFile f8("SignalHT-ttagUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f8.Close();

makeStack("ht", "isRegionD", "Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf*topSFDown(ptTopTagged)" );

TFile f9("SignalHT-ttagDown.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_LH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_LH");
h->Write();
f9.Close();




}
