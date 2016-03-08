void SignalHT_RH()
{
makeStack("ht", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)" );

TFile f1("SignalHT-RH-Nominal.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f1.Close();

/*
makeStack("ht", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"WtTrig(ht)*EvtWeight*EvtWtPV*EvtWtHTUp*btagsf*topSF(ptTopTagged)" );

TFile f2("SignalHT-RH-HTUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f2.Close();

makeStack("ht", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"WtTrig(ht)*EvtWeight*EvtWtPV*EvtWtHTDown*btagsf*topSF(ptTopTagged)" );

TFile f3("SignalHT-RH-HTDown.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f3.Close();
*/

makeStack("ht", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf_lUp*topSF(ptTopTagged)" );

TFile f4("SignalHT-RH-lUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f4.Close();

makeStack("ht", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf_lDown*topSF(ptTopTagged)" );

TFile f5("SignalHT-RH-lDown.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f5.Close();

makeStack("ht", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf_bcUp*topSF(ptTopTagged)" );

TFile f6("SignalHT-RH-bcUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f6.Close();

makeStack("ht", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf_bcDown*topSF(ptTopTagged)" );

TFile f7("SignalHT-RH-bcDown.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f7.Close();

makeStack("ht", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf*topSFUp(ptTopTagged)" );

TFile f8("SignalHT-RH-ttagUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f8.Close();

makeStack("ht", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 20, 1000, 2600,"EvtWeight*EvtWtPV*btagsf*topSFDown(ptTopTagged)" );

TFile f9("SignalHT-RH-ttagDown.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f9.Close();




}
