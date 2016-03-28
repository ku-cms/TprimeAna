#include "TROOT.h"
#include "TSystem.h"
#include "TCanvas.h"

void ANPlots()
{

gSystem->Load("./makeStack4_C.so");
TCanvas * c1;


//makeStack("PrunedMassAK8","ht>1100","Tprime1200_LH","Pruned Mass [GeV]","Jets","PrunedMass_noHTWt-Fig4",1,1,40,0,800,"EvtWeight*EvtWtPV");
//makeStack("tau2AK8/tau1AK8","ht>1100","Tprime1200_LH","#tau_{21}","Jets","tau21_noHTWt-Fig5",1,1,50,0,1,"EvtWeight*EvtWtPV");

//makeStack("min(sj0CSVAK8,sj1CSVAK8)","ht>1100&&(sj0CSVAK8>0.605||sj1CSVAK8>0.605)","Tprime1200_LH","subjet CSV","Jets","sjCSV2ndh_noHTWt-Fig6",1,1,50,0,1,"EvtWeight*EvtWtPV");
/*
makeStack("SoftDropMassAK8","ht>1100","Tprime1200_LH","SoftDropMass [Gev]","Jets","softDropMass_noHTWt-Fig7",1,1,40,0,800,"EvtWeight*EvtWtPV");
makeStack("tau3AK8/tau2AK8","ht>1100","Tprime1200_LH","#tau_{32}","Jets","tau32_noHTWt-Fig8",1,1,50,0,1,"EvtWeight*EvtWtPV");
makeStack("sj0CSVAK8","ht>1100","Tprime1200_LH","subjet CSV","Jets","sj0CSV_noHTWt-Fig9",1,1,50,0,1,"EvtWeight*EvtWtPV");
makeStack("sj1CSVAK8","ht>1100","Tprime1200_LH","subjet CSV","Jets","sj1CSV_noHTWt-Fig9",100,1,50,0,1,"EvtWeight*EvtWtPV");
makeStack("npv","ht>1100","Tprime1200_LH","nPV","Events","npv_noHTWt-Fig10",1,1,35,0,35,"EvtWeight*EvtWtPV");

makeStack("ht","ht>1100","Tprime1200_LH","H_{T} [GeV]","Events/80GeV","ht_noHTWt-Fig11",1,1,40,1100,2700,"EvtWeight*EvtWtPV");
makeStack("nAK4","ht>1100","Tprime1200_LH","# AK4 Jets","Events","nAK4_noHTWt-Fig12",1,1,20,0,20,"EvtWeight*EvtWtPV");
makeStack("nAK8","ht>1100","Tprime1200_LH","# AK4 Jets","Events","nAK8_noHTWt-Fig12",1,1,10,0,10,"EvtWeight*EvtWtPV");
makeStack("ptAK4","ht>1100","Tprime1200_LH","p_{T} AK4 Jets [GeV]","Jets/20 GeV","ptAK4_noHTWt-Fig13",1,1,35,0,700,"EvtWeight*EvtWtPV");
makeStack("ptAK8","ht>1100","Tprime1200_LH","p_{T} AK8 Jets [GeV]","Jets/20 GeV","ptAK8_noHTWt-Fig13",1,1,45,300,1200,"EvtWeight*EvtWtPV");
makeStack("etaAK4","ht>1100","Tprime1200_LH","#eta AK4 Jets","Jets","etaAK4_noHTWt-Fig14",1,1,50,-5,5,"EvtWeight*EvtWtPV");
makeStack("etaAK8","ht>1100","Tprime1200_LH","#eta AK8 Jets","Jets","etaAK8_Leading_noHTWt-Fig14",1,1,50,-5,5,"EvtWeight*EvtWtPV");
makeStack("ht","ht>1100","Tprime1200_LH","H_{T} [GeV]","Events/80GeV","ht_HTWt-Fig16",1,1,20,1100,2700,"EvtWeight*EvtWtPV*WeightHT(ht)");
makeStack("@ptHTagged.size()","ht>1100","Tprime1200_LH","# H Tags","Events","nHTag_noHTWt-Fig17",1,1,5,0,5,"EvtWeight*EvtWtPV");
makeStack("@ptTopTagged.size()","ht>1100","Tprime1200_LH","# Top Tags","Events","nTTag_noHTWt-Fig18",1,1,5,0,5,"EvtWeight*EvtWtPV");
// Figure 19: Cutflow - need to fix function
makeStack("ht","ht>1100&&isRegionD","Tprime1200_LH","H_{T} [GeV]","Events/80 GeV","ht_noHTWt-Fig20",1,1,20,1100,2700,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)");
makeStack("mtprime","ht>1100&&isRegionD","Tprime1200_LH","M_{T} [GeV]","Events/50 GeV","mt_noHTWt-Fig21",1,1,32,800,2400,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)");
//Figure 22 at bottom
//Figure 23 at bottom
makeStack("ht","ht>1100&&isRegionA","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionA_noHTWt-Fig25",1,1,20,1100,2700,"EvtWeight*EvtWtPV*btagsf");
makeStack("ht","ht>1100&&isRegionB","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionB_noHTWt-Fig25",1,1,20,1100,2700,"EvtWeight*EvtWtPV*topSF(ptTopTagged)*btagsf");
makeStack("ht","ht>1100&&isRegionC","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionC_noHTWt-Fig25",1,1,20,1100,2700,"EvtWeight*EvtWtPV*btagsf");




makeStack("nAK4","ht>1100","Tprime1200_LH","# AK4 Jets","Events","nAK4_HTWt-Fig30",1,1,20,0,20,"EvtWeight*EvtWtPV*WeightHT(ht)");
makeStack("nAK8","ht>1100","Tprime1200_LH","# AK4 Jets","Events","nAK8_HTWt-Fig30",1,1,10,0,10,"EvtWeight*EvtWtPV*WeightHT(ht)");

makeStack("ptAK4","ht>1100","Tprime1200_LH","p_{T} AK4 Jets [GeV]","Jets/20 GeV","ptAK4_HTWt-Fig31",1,1,35,0,700,"EvtWeight*EvtWtPV*WeightHT(ht)");
makeStack("ptAK8[idxAK8[0]]","ht>1100","Tprime1200_LH","p_{T} Leading AK8 Jets [GeV]","Jets/20 GeV","ptAK8_Leading_HTWt-Fig18",1,1,45,300,1200,"EvtWeight*EvtWtPV*WeightHT(ht)");
makeStack("etaAK4","ht>1100","Tprime1200_LH","#eta AK4 Jets","Jets","etaAK4_HTWt-Fig32",1,1,50,-5,5,"EvtWeight*EvtWtPV*WeightHT(ht)");
makeStack("etaAK8[idxAK8[0]]","ht>1100","Tprime1200_LH","#eta Leading AK8 Jets","Jets","etaAK8_Leading_HTWt-Fig32",1,1,50,-5,5,"EvtWeight*EvtWtPV*WeightHT(ht)");
makeStack("ht","ht>1100&&isRegionA","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionA_HTWt-Fig33",1,1,20,1100,2700,"EvtWeight*WeightHT(ht)*EvtWtPV*btagsf");
makeStack("ht","ht>1100&&isRegionB","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionB_HTWt-Fig33",1,1,20,1100,2700,"EvtWeight*WeightHT(ht)*EvtWtPV*topSF(ptTopTagged)*btagsf");
makeStack("ht","ht>1100&&isRegionC","Tprime1200_LH","H_{T} [GeV]", "Events/80 GeV","htRegionC_HTWt-Fig33",1,1,20,1100,2700,"EvtWeight*WeightHT(ht)*EvtWtPV*btagsf");
*/




/////////////////// ht weighting
/*
makeStack("PrunedMassAK8","ht>1100","Tprime1200_LH","Pruned Mass [GeV]","Jets","PrunedMass_HTWt-Fig4",1,1,40,0,800,"EvtWeight*WeightHT(ht)*EvtWtPV");
makeStack("tau2AK8/tau1AK8","ht>1100","Tprime1200_LH","#tau_{21}","Jets","tau21_HTWt-Fig5",1,1,50,0,1,"EvtWeight*WeightHT(ht)*EvtWtPV");
makeStack("min(sj0CSVAK8,sj1CSVAK8)","ht>1100&&(sj0CSVAK8>0.605||sj1CSVAK8>0.605)","Tprime1200_LH","subjet CSV","Jets","sjCSV2ndh_HTWt-Fig6",1,1,50,0,1,"EvtWeight*WeightHT(ht)*EvtWtPV");
makeStack("SoftDropMassAK8","ht>1100","Tprime1200_LH","SoftDropMass [Gev]","Jets","softDropMass_HTWt-Fig7",1,1,40,0,800,"EvtWeight*WeightHT(ht)*EvtWtPV");
makeStack("tau3AK8/tau2AK8","ht>1100","Tprime1200_LH","#tau_{32}","Jets","tau32_HTWt-Fig8",1,1,50,0,1,"EvtWeight*WeightHT(ht)*EvtWtPV");
makeStack("sj0CSVAK8","ht>1100","Tprime1200_LH","subjet CSV","Jets","sj0CSV_HTWt-Fig9",1,1,50,0,1,"EvtWeight*WeightHT(ht)*EvtWtPV");
makeStack("sj1CSVAK8","ht>1100","Tprime1200_LH","subjet CSV","Jets","sj1CSV_HTWt-Fig9",1,1,50,0,1,"EvtWeight*WeightHT(ht)*EvtWtPV");
makeStack("npv","ht>1100","Tprime1200_LH","nPV","Events","npv_HTWt-Fig10",1,1,35,0,35,"EvtWeight*WeightHT(ht)*EvtWtPV");
makeStack("@ptHTagged.size()","ht>1100","Tprime1200_LH","# H Tags","Events","nHTag_HTWt-Fig20",1,1,5,0,5,"EvtWeight*EvtWtPV*WeightHT(ht)");

makeStack("@ptTopTagged.size()","ht>1100","Tprime1200_LH","# Top Tags","Events","nTTag_HTWt-Fig21",1,1,5,0,5,"EvtWeight*EvtWtPV*WeightHT(ht)");
makeStack("ht","ht>1100&&isRegionD","Tprime1200_LH","H_{T} [GeV]","Events/80 GeV","ht_HTWt-Fig23",1,1,20,1100,2700,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)*WeightHT(ht)");

makeStack("mtprime","ht>1100&&isRegionD","Tprime1200_LH","M_{T} [GeV]","Events/50 GeV","mt_HTWt-Fig24",1,1,32,800,2400,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)*WeightHT(ht)");
*/



//////////////////////////




///////////////////////////

/*

makeStack("ht","ht>1100&&isRegionD","Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH","H_{T} [GeV]", "Events/80 GeV","ht_signalOnly_noHTWt",1,1,20,1100,2700,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)");
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
c1->Print("ht_noHTWt-Fig22.pdf");
c1->SaveAs("ht_noHTWt-Fig22.root");

makeStack("mtprime","ht>1100&&isRegionD","Tprime1200_LH;Tprime1000_LH;Tprime1500_LH;Tprime1800_LH", "M_{T} GeV", "Events/50 GeV", "" , 1,1, 36, 600,2400,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)");
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
c1->Print("mt_noHTWt-Fig22.pdf");
c1->SaveAs("mt_noHTWt-Fig22.root");

makeStack("ht","ht>1100&&isRegionD","Tprime1200_LH;Tprime1800_LH;Tprime1200_RH;Tprime1800_RH","H_{T} [GeV]", "Events/80 GeV","ht_signalOnly_noHTWt",1,1,20,1100,2700,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)");
TH1D *hSig13 = (TH1D*) gROOT->FindObject("Tprime1200_LH");
TH1D *hSig23 = (TH1D*) gROOT->FindObject("Tprime1800_LH");
TH1D *hSig33 = (TH1D*) gROOT->FindObject("Tprime1200_RH");
TH1D *hSig43 = (TH1D*) gROOT->FindObject("Tprime1800_RH");
TH1D *hBack3 = (TH1D*) gROOT->FindObject("hBack");

map<TString,TH1D*> signals3;

signals3.insert(make_pair(TString("Tprime1200_LH"),hSig13));
signals3.insert(make_pair(TString("Tprime1800_LH"),hSig23));
signals3.insert(make_pair(TString("Tprime1200_RH"),hSig33));
signals3.insert(make_pair(TString("Tprime1800_RH"),hSig43));
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Clear();

DrawPlot(c1,hBack3,0,signals3,0,0,0,0,1);
c1->Print("ht_noHTWt-Fig23.pdf");
c1->SaveAs("ht_noHTWt-Fig23.root");

makeStack("mtprime","ht>1100&&isRegionD","Tprime1200_LH;Tprime1800_LH;Tprime1200_RH;Tprime1800_RH", "M_{T} GeV", "Events/50 GeV", "" , 1,1, 36, 600,2400,"EvtWeight*EvtWtPV*btagsf*topSF(ptTopTagged)");
TH1D *hSig14 = (TH1D*) gROOT->FindObject("Tprime1200_LH");
TH1D *hSig24 = (TH1D*) gROOT->FindObject("Tprime1800_LH");
TH1D *hSig34 = (TH1D*) gROOT->FindObject("Tprime1200_RH");
TH1D *hSig44 = (TH1D*) gROOT->FindObject("Tprime1800_RH");
TH1D *hBack4 = (TH1D*) gROOT->FindObject("hBack");

map<TString,TH1D*> signals4;

signals4.insert(make_pair(TString("Tprime1200_LH"),hSig14));
signals4.insert(make_pair(TString("Tprime1800_LH"),hSig24));
signals4.insert(make_pair(TString("Tprime1200_RH"),hSig34));
signals4.insert(make_pair(TString("Tprime1800_RH"),hSig44));
c1 = (TCanvas * ) gROOT->FindObject("c1");
c1->Clear();

DrawPlot(c1,hBack2,0,signals2,0,0,0,0,1);
c1->Print("mt_noHTWt-Fig23.pdf");
c1->Print("mt_noHTWt-Fig23.root");
*/
makeStack("ht", "Sum$(abs(etaAK4)>2.4)==0" ,"Tprime1200_LH","HT GeV","Events","HT-FJ-No24",1000,1,40,1000,2600,"EvtWeight*EvtWtPV");
makeStack("ht", "Sum$(abs(etaAK4)>2.4)>0" ,"Tprime1200_LH","HT GeV","Events","HT-FJ-24",1000,1,40,1000,2600,"EvtWeight*EvtWtPV");
}
