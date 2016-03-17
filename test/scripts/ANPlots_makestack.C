#include "TROOT.h"
#include "TSystem.h"
#include "TCanvas.h"

void ANPlots()
{

gSystem->Load("./makeStack4_C.so");
TCanvas * c1;
/*
makeStack("ht","ht>1100&&isRegionA","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionA_noHTWt-Fig28",1,1,19,1100,2600,"EvtWeight*EvtWtPV");
makeStack("ht","ht>1100&&isRegionB","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionB_noHTWt-Fig28",1,1,19,1100,2600,"EvtWeight*EvtWtPV*topSF(ptTopTagged)");
makeStack("ht","ht>1100&&isRegionC","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionC_noHTWt-Fig28",1,1,19,1100,2600,"EvtWeight*EvtWtPV*btagsf");

makeStack("npv","ht>1100","Tprime1200_LH","nPV","Events","npv_noHTWt-Fig10",1000,1,35,0,35,"EvtWeight*EvtWtPV");

makeStack("tau3AK8/tau2AK8","ht>1100","Tprime1200_LH","#tau_{32}","Jets","tau32_noHTWt-Fig8",1000,1,50,0,1,"EvtWeight*EvtWtPV");

makeStack("SoftDropMassAK8","ht>1100","Tprime1200_LH","SoftDropMass [Gev]","Jets","softDropMass_noHTWt-Fig7",1,1,40,0,800,"EvtWeight*EvtWtPV");

makeStack("min(sj0CSVAK8,sj1CSVAK8)","ht>1100&&(sj0CSVAK8>0.605||sj1CSVAK8>0.605)","Tprime1200_LH","subjet CSV","Jets","sjCSV2ndh_noHTWt-Fig6",1000,1,50,0,1,"EvtWeight*EvtWtPV");

makeStack("sj0CSVAK8","ht>1100","Tprime1200_LH","subjet CSV","Jets","sj0CSV_noHTWt-Fig9",1000,1,50,0,1,"EvtWeight*EvtWtPV");

makeStack("sj1CSVAK8","ht>1100","Tprime1200_LH","subjet CSV","Jets","sj1CSV_noHTWt-Fig9",1000,1,50,0,1,"EvtWeight*EvtWtPV");

makeStack("tau2AK8/tau1AK8","ht>1100","Tprime1200_LH","#tau_{21}","Jets","tau21_noHTWt-Fig5",1000,1,50,0,1,"EvtWeight*EvtWtPV");

makeStack("PrunedMassAK8","ht>1100","Tprime1200_LH","Pruned Mass [GeV]","Jets","PrunedMass_noHTWt-Fig4",1,1,40,0,800,"EvtWeight*EvtWtPV");

///////////////////
makeStack("ht","ht>1100&&isRegionA","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionA_HTWt-Fig28",1,1,19,1100,2600,"EvtWeight*WeightHT(ht)*EvtWtPV");
makeStack("ht","ht>1100&&isRegionB","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionB_HTWt-Fig28",1,1,19,1100,2600,"EvtWeight*WeightHT(ht)*EvtWtPV*topSF(ptTopTagged)");
makeStack("ht","ht>1100&&isRegionC","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionC_HTWt-Fig28",1,1,19,1100,2600,"EvtWeight*WeightHT(ht)*EvtWtPV*btagsf");

makeStack("npv","ht>1100","Tprime1200_LH","nPV","Events","npv_HTWt-Fig10",1000,1,35,0,35,"EvtWeight*WeightHT(ht)*EvtWtPV");

makeStack("tau3AK8/tau2AK8","ht>1100","Tprime1200_LH","#tau_{32}","Jets","tau32_HTWt-Fig8",1000,1,50,0,1,"EvtWeight*WeightHT(ht)*EvtWtPV");

makeStack("SoftDropMassAK8","ht>1100","Tprime1200_LH","SoftDropMass [Gev]","Jets","softDropMass_HTWt-Fig7",1,1,40,0,800,"EvtWeight*WeightHT(ht)*EvtWtPV");

makeStack("min(sj0CSVAK8,sj1CSVAK8)","ht>1100&&(sj0CSVAK8>0.605||sj1CSVAK8>0.605)","Tprime1200_LH","subjet CSV","Jets","sjCSV2ndh_HTWt-Fig6",1000,1,50,0,1,"EvtWeight*WeightHT(ht)*EvtWtPV");

makeStack("sj0CSVAK8","ht>1100","Tprime1200_LH","subjet CSV","Jets","sj0CSV_HTWt-Fig9",1000,1,50,0,1,"EvtWeight*WeightHT(ht)*EvtWtPV");

makeStack("sj1CSVAK8","ht>1100","Tprime1200_LH","subjet CSV","Jets","sj1CSV_HTWt-Fig9",1000,1,50,0,1,"EvtWeight*WeightHT(ht)*EvtWtPV");

makeStack("tau2AK8/tau1AK8","ht>1100","Tprime1200_LH","#tau_{21}","Jets","tau21_HTWt-Fig5",1000,1,50,0,1,"EvtWeight*WeightHT(ht)*EvtWtPV");

makeStack("PrunedMassAK8","ht>1100","Tprime1200_LH","Pruned Mass [GeV]","Jets","PrunedMass_HTWt-Fig4",1,1,40,0,800,"EvtWeight*WeightHT(ht)*EvtWtPV");

//////////////////////////

makeStack("ht","ht>1100","Tprime1200_LH","H_{T} [GeV]","Events/80GeV","ht_noHTWt-Fig11",1000,1,19,1100,2600,"EvtWeight*EvtWtPV");

makeStack("nAK4","ht>1100","Tprime1200_LH","# AK4 Jets","Events","nAK4_noHTWt-Fig12",1,1,10,0,10,"EvtWeight*EvtWtPV");
makeStack("nAK8","ht>1100","Tprime1200_LH","# AK4 Jets","Events","nAK8_noHTWt-Fig12",1,1,10,0,10,"EvtWeight*EvtWtPV");

makeStack("ptAK4","ht>1100","Tprime1200_LH","p_{T} AK4 Jets [GeV]","Jets/20 GeV","ptAK4_noHTWt-Fig13",1000,1,35,0,700,"EvtWeight*EvtWtPV");
makeStack("ptAK8[idxAK8[0]]","ht>1100","Tprime1200_LH","p_{T} Leading AK8 Jets [GeV]","Jets/20 GeV","ptAK8_Leading_noHTWt-Fig13",1000,1,35,0,700,"EvtWeight*EvtWtPV");

makeStack("etaAK4","ht>1100","Tprime1200_LH","#eta AK4 Jets","Jets","etaAK4_noHTWt-Fig14",1000,1,50,-5,5,"EvtWeight*EvtWtPV");
makeStack("etaAK8[idxAK8[0]]","ht>1100","Tprime1200_LH","#eta Leading AK8 Jets","Jets","etaAK8_Leading_noHTWt-Fig14",1000,1,50,-5,5,"EvtWeight*EvtWtPV");

makeStack("ht","ht>1100","Tprime1200_LH","H_{T} [GeV]","Events/80GeV","ht_HTWt-Fig16",1000,1,19,1100,2600,"EvtWeight*EvtWtPV*WeightHT(ht)");

makeStack("nAK4","ht>1100","Tprime1200_LH","# AK4 Jets","Events","nAK4_HTWt-Fig17",1,1,10,0,10,"EvtWeight*EvtWtPV*WeightHT(ht)");
makeStack("nAK8","ht>1100","Tprime1200_LH","# AK4 Jets","Events","nAK8_HTWt-Fig17",1,1,10,0,10,"EvtWeight*EvtWtPV*WeightHT(ht)");


makeStack("ptAK4","ht>1100","Tprime1200_LH","p_{T} AK4 Jets [GeV]","Jets/20 GeV","ptAK4_HTWt-Fig18",1000,1,35,0,700,"EvtWeight*EvtWtPV*WeightHT(ht)");
makeStack("ptAK8[idxAK8[0]]","ht>1100","Tprime1200_LH","p_{T} Leading AK8 Jets [GeV]","Jets/20 GeV","ptAK8_Leading_HTWt-Fig18",1000,1,35,0,700,"EvtWeight*EvtWtPV*WeightHT(ht)");

makeStack("etaAK4","ht>1100","Tprime1200_LH","#eta AK4 Jets","Jets","etaAK4_HTWt-Fig19",1000,1,50,-5,5,"EvtWeight*EvtWtPV*WeightHT(ht)");
makeStack("etaAK8[idxAK8[0]]","ht>1100","Tprime1200_LH","#eta Leading AK8 Jets","Jets","etaAK8_Leading_HTWt-Fig19",1000,1,50,-5,5,"EvtWeight*EvtWtPV*WeightHT(ht)");


//makeStack("ptHTagged.Size()","ht>1100&&","Tprime1200_LH","# H Tags","Events","nHTag_noHTWt-Fig20",1,1,5,0,5,"EvtWeight*EvtWtPV");

//makeStack("ptTopTagged.Size()","ht>1100&&","Tprime1200_LH","# Top Tags","Events","nTTag_noHTWt-Fig21",1,1,5,0,5,"EvtWeight*EvtWtPV");


makeStack("ht","ht>1100&&isRegionD","Tprime1200_LH","H_{T} [GeV]","Events/80 GeV","ht_noHTWt-Fig23",1,1,19,1100,2600,"EvtWeight*EvtWtPV");

makeStack("mtprime","ht>1100&&isRegionD","Tprime1200_LH","M_{T} [GeV]","Events/50 GeV","mt_noHTWt-Fig24",1,1,32,800,2400,"EvtWeight*EvtWtPV");
///////////////////////////
//makeStack("ptHTagged.Size()","ht>1100&&","Tprime1200_LH","# H Tags","Events","nHTag_HTWt-Fig20",1,1,5,0,5,"EvtWeight*EvtWtPV");

//makeStack("ptTopTagged.Size()","ht>1100&&","Tprime1200_LH","# Top Tags","Events","nTTag_HTWt-Fig21",1,1,5,0,5,"EvtWeight*EvtWtPV");


makeStack("ht","ht>1100&&isRegionD","Tprime1200_LH","H_{T} [GeV]","Events/80 GeV","ht_HTWt-Fig23",1,1,20,1100,2600,"EvtWeight*EvtWtPV");
*/
makeStack("mtprime","ht>1100&&isRegionD","Tprime1200_LH","M_{T} [GeV]","Events/50 GeV","mt_HTWt-Fig24",1,1,32,800,2400,"EvtWeight*EvtWtPV");


makeStack("ht","ht>1100&&isRegionD","Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH","H_{T} [GeV]", "Events/80 GeV","ht_signalOnly_noHTWt",1,1,19,1100,2600,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)");
TH1D *hSig1 = (TH1D*) gROOT->FindObject("Tprime1000_LH");
TH1D *hSig2 = (TH1D*) gROOT->FindObject("Tprime1200_LH");
TH1D *hSig3 = (TH1D*) gROOT->FindObject("Tprime1500_LH");
TH1D *hSig4 = (TH1D*) gROOT->FindObject("Tprime1800_LH");
TH1D *hBack = (TH1D*) gROOT->FindObject("hBack");

map<TString,TH1D*> signals;

signals.insert(make_pair(TString("Tprime1000_LH"),hSig1));
signals.insert(make_pair(TString("Tprime1200_LH"),hSig2));
signals.insert(make_pair(TString("Tprime1500_LH"),hSig3));
signals.insert(make_pair(TString("Tprime1800_LH"),hSig4));
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Clear();

DrawPlot(c1,hBack,0,signals,0,0,0,0,1);
c1->Print("ht_noHTWt-Fig25.pdf");
c1->SaveAs("ht_noHTWt-Fig25.root");

makeStack("mtprime","isRegionD","Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "M_{T} GeV", "Events/50 GeV", "" , 1,1, 36, 600,2400,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)");
TH1D *hSig12 = (TH1D*) gROOT->FindObject("Tprime1000_LH");
TH1D *hSig22 = (TH1D*) gROOT->FindObject("Tprime1200_LH");
TH1D *hSig32 = (TH1D*) gROOT->FindObject("Tprime1500_LH");
TH1D *hSig42 = (TH1D*) gROOT->FindObject("Tprime1800_LH");
TH1D *hBack2 = (TH1D*) gROOT->FindObject("hBack");

map<TString,TH1D*> signals2;

signals2.insert(make_pair(TString("Tprime1000_LH"),hSig12));
signals2.insert(make_pair(TString("Tprime1200_LH"),hSig22));
signals2.insert(make_pair(TString("Tprime1500_LH"),hSig32));
signals2.insert(make_pair(TString("Tprime1800_LH"),hSig42));
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Clear();

DrawPlot(c1,hBack2,0,signals2,0,0,0,0,1);
c1->Print("mt_noHTWt-Fig26.pdf");
c1->SaveAs("mt_noHTWt-Fig26.root");

}
