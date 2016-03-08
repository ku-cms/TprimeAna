void SignalMT_RH()
{
makeStack("mtprime", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 36, 600, 2400,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)" );

TFile f1("SignalMT-RH-Nominal.root","RECREATE");
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
makeStack("mtprime", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 36, 600, 2400,"WtTrig(ht)*EvtWeight*EvtWtPV*EvtWtHTUp*btagsf*topSF(ptTopTagged)" );

TFile f2("SignalMT-HTUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f2.Close();

makeStack("mtprime", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 36, 600, 2400,"WtTrig(ht)*EvtWeight*EvtWtPV*EvtWtHTDown*btagsf*topSF(ptTopTagged)" );

TFile f3("SignalMT-HTDown.root","RECREATE");
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

makeStack("mtprime", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 36, 600, 2400,"EvtWeight*EvtWtPV*btagsf_lUp*topSF(ptTopTagged)" );

TFile f4("SignalMT-RH-lUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f4.Close();

makeStack("mtprime", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 36, 600, 2400,"EvtWeight*EvtWtPV*btagsf_lDown*topSF(ptTopTagged)" );

TFile f5("SignalMT-RH-lDown.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f5.Close();

makeStack("mtprime", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 36, 600, 2400,"EvtWeight*EvtWtPV*btagsf_bcUp*topSF(ptTopTagged)" );

TFile f6("SignalMT-RH-bcUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f6.Close();

makeStack("mtprime", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 36, 600, 2400,"EvtWeight*EvtWtPV*btagsf_bcDown*topSF(ptTopTagged)" );

TFile f7("SignalMT-RH-bcDown.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f7.Close();

makeStack("mtprime", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 36, 600, 2400,"EvtWeight*EvtWtPV*btagsf*topSFUp(ptTopTagged)" );

TFile f8("SignalMT-RH-ttagUp.root","RECREATE");
h = (TH1D*) gROOT->FindObject("Tprime1800_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1500_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1000_RH");
h->Write();
h = (TH1D*) gROOT->FindObject("Tprime1200_RH");
h->Write();
f8.Close();

makeStack("mtprime", "isRegionD", "Tprime1200_RH;Tprime1000_RH;Tprime1500_RH;Tprime1800_RH", "HT GeV", "Events", "Cut D", 1, 1, 36, 600, 2400,"EvtWeight*EvtWtPV*btagsf*topSFDown(ptTopTagged)" );

TFile f9("SignalMT-RH-ttagDown.root","RECREATE");
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
