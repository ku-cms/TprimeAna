
#include "TH1D.h"
#include "TFile.h"
#include "TTree.h"
#include "TCanvas.h"
#include "THStack.h"
#include "TLegend.h"
#include "TChain.h"
#include "TF1.h"
#include "TStyle.h"
#include "TString.h"
#include "TLorentzVector.h"
#include "DataFormats/Math/interface/deltaR.h"
#include <iostream>
#include "TROOT.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TGraphAsymmErrors.h"
#include "TLatex.h"


using namespace std;

void ratioPlot( TCanvas *, THStack *, TH1D *);
void ratioPlot(TCanvas * c1 , TH1D * , TH1D * );
  
TGraphAsymmErrors * wGraph = 0;
TH1D * PUcorr = 0;

double PUWeight(int inpu)
{
  if ( PUcorr == 0 ) {
       TFile * pufile = new TFile("PUcorrection.root");
       PUcorr = (TH1D*) pufile->Get("pileup");
  }

  return  PUcorr->GetBinContent(inpu+1);


}


double topSFVal(double TopPT, int shift)
{


   if( TopPT >= 400. && TopPT < 550.) {
      if(shift == 0 ) return 0.88 ;
      if(shift == 1 ) return 0.88+0.13 ; 
      if(shift == -1) return 0.88-0.13;
    }
    else if ( TopPT  >= 550.)  {
      if(shift == 0 ) return 0.94 ;
      if(shift == 1 ) return 0.94+0.29 ; 
      if(shift == -1) return 0.94-0.29;
    }
	return 1;
}
double topSF(double TopPT)
{
	return topSFVal(TopPT,0);
}

double topSFUp(double TopPT)
{
	return topSFVal(TopPT,1);
}
double topSFDown(double TopPT)
{
	return topSFVal(TopPT,-1);
}



double WtTrig(double HT)
{
   if (wGraph == 0)
   {
	TFile * wf = new TFile("eff_JetHT_PromptRecov4_htak4_HLT_PFHT800_v-2.root","READ");
	
      	wGraph = (TGraphAsymmErrors * ) wf->Get("eff_htak4_HLT_PFHT800_v");

	cout << "Loaded weights..." << endl;
   }
	
    return wGraph->Eval(HT);
 

}


double WeightHT(double HT) 
{

//Fit between 1000 and 2400
//Chi2: 34.6
//Par0: 0.25+/-0.02
//Par1: -0.00025+/-0.000012

	if(HT < 1100 || HT > 2600)
		return 1;
	else
		return (1+(-0.0001961*HT + 0.262));
	
}


void DrawPlot( TCanvas * c1, TH1D * hBack, TH1D * hData, std::map<TString,TH1D*> &hSignal, TH1D * hQCD = 0, TH1D * histW = 0, TH1D * histTT = 0, TH1D * histST = 0 )
{


	TString lumiText = "2.2 fb^{-1} (13 TeV)";
	TString cmsText = "#bf{CMS}";
	TString extraText = "Preliminary";

	

      	TPad *pad1 = new TPad("pad1","pad1",0,0.2,1,1);
      	pad1->SetBottomMargin(0.13);
      	pad1->SetTopMargin(0.05);


	TLatex latex;
  	latex.SetNDC();
  	latex.SetTextAngle(0);
  	latex.SetTextColor(kBlack);

  	//float extraTextSize = extraOverCmsTextSize*cmsTextSize;
      	pad1->Draw();
      	pad1->cd();

  	latex.SetTextFont(42);
  	latex.SetTextAlign(31);
  	latex.SetTextSize(.04);


	if(hQCD) hQCD->SetFillColor(kCyan);
	if(histW) histW->SetFillColor(kGreen);
	if(histTT) histTT->SetFillColor(kBlue);
	
	Int_t yMax = 0;

	if(hBack) {
		for(unsigned i = 0 ; i < unsigned(hBack->GetNbinsX()) ; i++) 
		{

	    		if (hBack->GetBinContent(i) > yMax)
			yMax = hBack->GetBinContent(i);
		}
	}
	
	// Don't draw stack if only hBack provided.
	
	if(histW && histTT && hQCD && histST)  {
	
		THStack * hs = new THStack( "hsBack",hBack->GetTitle());
	
		histW->SetMarkerStyle(0);
		histTT->SetMarkerStyle(0);
		hQCD->SetMarkerStyle(0);
		histST->SetMarkerStyle(0);
		
		hs->Add(histW,"hist");
		hs->Add(histTT,"hist");
		hs->Add(hQCD,"hist");
		hs->Add(histST,"hist");

		//cout << "QCD = " << hQCD->Integral(0,1000) << endl;
		//cout << "TTJets = " << histTT->Integral(0,1000) << endl;
		//cout << "WJets = " << histW->Integral(0,1000) << endl;
	
		hs->SetMaximum(yMax*1.6);
		hs->SetMinimum(0.01);
		hs->Draw("hist");//F

		//Set Axis Labels and size from passed Histogram.
	
		hs->GetHistogram()->GetYaxis()->SetTitle(hBack->GetYaxis()->GetTitle());
		hs->GetHistogram()->GetYaxis()->SetTitleSize(hBack->GetYaxis()->GetTitleSize());
		hs->GetHistogram()->GetYaxis()->SetTitleOffset(hBack->GetYaxis()->GetTitleOffset());
		hs->GetHistogram()->GetXaxis()->SetTitle(hBack->GetXaxis()->GetTitle());
	
	}
	
	TH1D* hBackErr =0; 
	if(hBack) {
		hBackErr = (TH1D*) hBack->Clone("hBackErr"); 
		hBackErr->SetMarkerStyle(0);
		hBackErr->SetFillColor(kGray+2);
  		hBackErr->SetFillStyle(3018);
  		hBackErr->Draw("e2same");
		hBack->SetFillStyle(0);
  	        hBack->Draw("hist same");
	}

	if(hData) {
        	hData->SetLineColor(kBlack);
        	//hData->SetMarkerStyle(20);
        	hData->Draw("L same"); // "L same"
	}
	double x0 = 0.6;
	double x1 = 0.8;

	// Find best position for Legend.
	if(hBack) {
	   if(hBack->GetMaximumBin() > hBack->GetXaxis()->GetNbins() * .4){
		x0 = .2;
		x1 = .4;
	   }
	   else {
		x0 = 0.6;
		x1 = 0.8;	
	   }
	}
        TLegend * leg = new TLegend(x0,0.6,x1,0.85);

	//Draw signal histos from vector.
	int cnt = 0;
	if ( hSignal.size() > 0 ) {
	    for( std::map< TString, TH1D* >::iterator it = hSignal.begin() ; it != hSignal.end(); it++ ) {
		it->second->SetLineColor(kRed+cnt);
		it->second->SetMarkerStyle(0);
		it->second->Draw("hist same"); 
		leg->AddEntry(it->second,it->first);
		double integral, err;
		integral = it->second->IntegralAndError(0,1000,err);
		cout << it->first << " = " << integral << " +/- " << err << endl;
		cnt++;
	    }
	}

	if( hQCD ) {

        	leg->AddEntry(hQCD,"QCD");
        	leg->AddEntry(histW,"WJets");
        	leg->AddEntry(histTT,"TTJets");
        	leg->AddEntry(histST,"SingleTop");
	}
        if(hData) leg->AddEntry(hData,"2015D Data");
	if(hBack) {
		leg->AddEntry(hBackErr,"Stat.+x-sec unc.","F");
	}	


//	if(hSignal != 0)
//            leg->AddEntry(hSignal,"Tprime (M1200) x 100 ");

        leg->Draw();

        if(hData) ratioPlot(c1, hBack, hData);

//	CMS_lumi(c1,4,33);
/*
	c1->Update();
	c1->RedrawAxis();
	c1->GetFrame()->Draw();
*/
	pad1->cd();

  	latex.DrawLatex(.8,.96,lumiText);
	latex.DrawLatex(x0,.89,cmsText);
	latex.DrawLatex(x1,.86,extraText);
	
}


TString Tprimemass(Int_t HIdx, Int_t TIdx)
{
	TString out;
	out.Form("mass(ptAK8[%d],etaAK8[%d],phiAK8[%d],MAK8[%d],ptAK8[%d],etaAK8[%d],phiAK8[%d],MAK8[%d])",HIdx,HIdx,HIdx,HIdx,TIdx,TIdx,TIdx,TIdx);
	return out;
}

double dR(double eta1,double phi1, double eta2, double phi2) {

	return deltaR(eta1,phi1,eta2,phi2);
}


double mass(double pt1, double eta1, double phi1 ,double m1, double pt2, double eta2, double phi2, double m2 )
{

                TLorentzVector TCand, HCand;

                HCand.SetPtEtaPhiM(pt1,
                         eta1,
                         phi1,
                         m1);

                TCand.SetPtEtaPhiM(pt2,
                         eta2,
                         phi2,
                         m2);
                return (HCand + TCand).M();
 

}


double makeStack(TString plot,TString cuts, TString Signal, TString label, TString yLabel, TString title,int sigScale = 1, int rebin = 1,int bins=1000, int xMin=0, int xMax=1000, TString sScale="1",bool bSep = false, bool bData = true, TString sExt="")
{
	gROOT->Clear();
	//TString sPath = "/home/t3-ku/stringer/CMSSW_7_4_8_patch1/src/UserCode/TprimeAna/test/Selection0308/";
        TString sPath = "/home/t3-ku/erichjs/work/B2G/CMSSW_7_4_8_patch1/src/TprimeAna/test/Selection0307/";
	TH1::SetDefaultSumw2();

	TChain * tree2 = new TChain("ana/tree");
	TChain * tree6 = new TChain("ana/tree");
	TChain * tree7 = new TChain("ana/tree");
	TChain * tree8 = new TChain("ana/tree");
	TChain * tree9 = new TChain("ana/tree");
	TChain * tree10 = new TChain("ana/tree");
	TChain * tree11 = new TChain("ana/tree");
	TChain * tree12 = new TChain("ana/tree");

	TChain * treeData = new TChain("ana/tree");

	//cout << "Data files: " << treeData->Add(sPath+"../Selection0307/JetHT_Prompt.root") << endl;
	//cout << "Data files: " << treeData->Add(sPath+"../Selection0307/JetHT_05Oct.root") << endl;
	cout << "Data files: " << treeData->Add(sPath+"JetHT_Prompt.root") << endl;
	cout << "Data files: " << treeData->Add(sPath+"JetHT_05Oct.root") << endl;

	std::map<TChain* , TString> fSig ;
	std::map<TString , double> nEvts;	

	TObjArray * sigNames = Signal.Tokenize(TString(";"));

        sigNames->Print();
        for (Int_t i = 0; i < sigNames->GetEntries(); i++) {

                TString s = ((TObjString *)(sigNames->At(i)))->String();
		if (s != ""){
			TFile f(sPath+s+sExt+".root");
			TH1D * temp = (TH1D*) f.Get("allEvents/hEventCount_wt");
			nEvts.insert(make_pair(s,temp->Integral(0,10000)));
			f.Close();
			TChain * t = new TChain("ana/tree"); 			
			t->Add(sPath+s+sExt+".root");
			s.ReplaceAll("*","");
			TString ScaleNoHT(sScale);
			ScaleNoHT = ScaleNoHT.ReplaceAll("EvtWtHTUp*","");
			ScaleNoHT = ScaleNoHT.ReplaceAll("EvtWtHTDown*","");
			ScaleNoHT = ScaleNoHT.ReplaceAll("EvtWtHT*","");
                	cout << "Scale: " << ScaleNoHT << endl;

			TH1D *histSig = new TH1D(s,"",bins,xMin,xMax);
			t->Draw(plot+">>"+s,ScaleNoHT+"*("+cuts+")");
			cout << "Plotting " << s <<endl;
			fSig.insert(make_pair(t,s));
		}
	}
	//Get number of events.
	
        TFile * fTT = new TFile (sPath+"TTJets_powheg"+sExt+".root","READ");
        TFile * f700 = new TFile (sPath+"QCDHT700"+sExt+".root","READ");
        TFile * f1000 = new TFile (sPath+"QCDHT1000"+sExt+".root","READ");
        TFile * f1500 = new TFile (sPath+"QCDHT1500"+sExt+".root","READ");
        TFile * f2000 = new TFile (sPath+"QCDHT2000"+sExt+".root","READ");
        TFile * fW = new TFile (sPath+"WJets"+sExt+".root","READ");
        TFile * fSTT = new TFile (sPath+"ST_top"+sExt+".root","READ");
        TFile * fSTaT = new TFile (sPath+"ST_antitop"+sExt+".root","READ");

	TH1D * tempTT = (TH1D*) fTT->Get("allEvents/hEventCount_wt");
	TH1D * temp700 = (TH1D*) f700->Get("allEvents/hEventCount_wt");
	TH1D * temp1000 = (TH1D*) f1000->Get("allEvents/hEventCount_wt");
	TH1D * temp1500 = (TH1D*) f1500->Get("allEvents/hEventCount_wt");
	TH1D * temp2000 = (TH1D*) f2000->Get("allEvents/hEventCount_wt");
	TH1D * tempW = (TH1D*) fW->Get("allEvents/hEventCount_wt");
	TH1D * tempSTT = (TH1D*) fSTT->Get("allEvents/hEventCount_wt");
	TH1D * tempSTaT = (TH1D*) fSTaT->Get("allEvents/hEventCount_wt");

        nEvts.insert(make_pair("TTJets",tempTT->Integral(0,10000)));
        nEvts.insert(make_pair("QCDHT700",temp700->Integral(0,10000)));
        nEvts.insert(make_pair("QCDHT1000",temp1000->Integral(0,10000)));
        nEvts.insert(make_pair("QCDHT1500",temp1500->Integral(0,10000)));
        nEvts.insert(make_pair("QCDHT2000",temp2000->Integral(0,10000)));
        nEvts.insert(make_pair("WJets",tempW->Integral(0,10000)));
        nEvts.insert(make_pair("ST",tempSTT->Integral(0,10000)+tempSTaT->Integral(0,10000)));
	

        fTT->Close();
        f700->Close();
        f1000->Close();
        f1500->Close();
        f2000->Close();
        fW->Close();
	fSTT->Close();
	fSTaT->Close();
	
	delete fTT;
	delete f700;
	delete f1000;
	delete f1500;
	delete f2000;
	delete fSTT;
	delete fSTaT;

	cout << "TTJets: " << nEvts["TTJets"] <<endl;
	cout << "700: " << nEvts["QCDHT700"] <<endl;
	
	// 

        tree2->Add(sPath+"TTJets_powheg"+sExt+".root");
        //TFile * f3 = new TFile ("QCDHT100v2.root","READ");
        //TFile * f4 = new TFile ("QCDHT200v2.root","READ");
        //TFile * f5 = new TFile ("QCDHT300v2.root","READ");
	//cout << "QCD500: " << tree6->Add("QCDHT500v2*.root") << endl;
        cout << "QCD700: " << tree7->Add(sPath+"QCDHT700"+sExt+".root") << endl ;
        cout << "QCD1000: " << tree8->Add(sPath+"QCDHT1000"+sExt+".root") << endl;
        cout << "QCD1500: " << tree9->Add(sPath+"QCDHT1500"+sExt+".root") << endl;
        cout << "QCD2000: " << tree10->Add(sPath+"QCDHT2000"+sExt+".root") << endl;
        cout << "WJets: " << tree11->Add(sPath+"WJets"+sExt+".root") << endl;
	cout << "STtop: " << tree12->Add(sPath+"ST_top"+sExt+".root") << endl;
        cout << "STantitop: " << tree12->Add(sPath+"ST_antitop"+sExt+".root") << endl;
  	
        gStyle->SetOptStat(0);

        //TH1D * hist1 = new TH1D("ht1","",bins,xMin,xMax);
	TH1D * hist2= new TH1D("ht2","",bins,xMin,xMax);
	//TH1D * hist3= new TH1D("ht3","",bins,xMin,xMax);
	//TH1D * hist4= new TH1D("ht4","",bins,xMin,xMax);
        //TH1D * hist5= new TH1D("ht5","",bins,xMin,xMax);
	//TH1D * hist6= new TH1D("ht6","",bins,xMin,xMax);
	TH1D * hist7= new TH1D("ht7","",bins,xMin,xMax);
	TH1D * hist8 = new TH1D("ht8","",bins,xMin,xMax);
	TH1D * hist9 = new TH1D("ht9","",bins,xMin,xMax);
        TH1D *hist10 = new TH1D("ht10","",bins,xMin,xMax);
	TH1D *hist11 = new TH1D("ht11","",bins,xMin,xMax);
	TH1D *hist12 = new TH1D("ht12","",bins,xMin,xMax);
	TH1D *histData = new TH1D("htdata","",bins,xMin,xMax);
        histData->SetBinErrorOption(TH1::kPoisson);



/*    
        TH1D * hist1 = new TH1D("ht1","HT",1000,0,2000);
	TH1D * hist2= new TH1D("ht2","HT",1000,0,2000);
	TH1D * hist3= new TH1D("ht3","HT",1000,0,2000);
	TH1D * hist4= new TH1D("ht4","HT",1000,0,2000);
        TH1D * hist5= new TH1D("ht5","HT",1000,0,2000);
	TH1D * hist6= new TH1D("ht6","HT",1000,0,2000);
	TH1D * hist7= new TH1D("ht7","HT",1000,0,2000);
	TH1D * hist8 = new TH1D("ht8","HT",1000,0,2000);
	TH1D * hist9 = new TH1D("ht9","HT",1000,0,2000);
        TH1D *hist10 = new TH1D("ht10","HT",1000,0,2000);
	TH1D *hist11 = new TH1D("ht11","HT",1000,0,2000);
	TH1D *histData = new TH1D("htdata","HT",1000,0,2000);;
*/


	//hist1->Rebin(rebin);
	hist2->Rebin(rebin);
	//hist3->Rebin(rebin);
	//hist4->Rebin(rebin);
	//hist5->Rebin(rebin);
	//hist6->Rebin(rebin);
	hist7->Rebin(rebin);
	hist8->Rebin(rebin);
	hist9->Rebin(rebin);
	hist10->Rebin(rebin);
	hist11->Rebin(rebin);
	hist12->Rebin(rebin);
	histData->Rebin(rebin);

	THStack * hs = new THStack("hs","SideBand");
/*
	map<TChain *, TString> sigTrees;
	for( std::map<TFile *, TString>::iterator it = fSig.begin() ; it != fSig.end() ; it++) { 	
		TH1D *histSig = new TH1D(it->second,"Signal",bins,xMin,xMax);
		TFile * f = it->first;
        	TTree * t = (TTree*) f->Get("ana/Tree");
		TString ScaleNoHT = sScale;
		//ScaleNoHT = ScaleNoHT.ReplaceAll("*WeightHT(htak4)","");
		cout << "Scale: " << ScaleNoHT << endl;
		t->Draw(plot+">>"+it->second,ScaleNoHT+"*("+cuts+")");
	}
*/
	double csSig[11] = {
                0.054,  //800
                0.026,  //900
                0.030,  //1000
                0.034,  //1100
                0.037,  //1200
                0.053,  //1300
                0.056,  //1400
                0.052,  //1500
                0.052,  //1600
                0.038,   //1700
                0.038   //1700
        };


//        TTree * tree2 = (TTree*) f2->Get("analyze/cutTree");
        //TTree * tree3 = (TTree*) f3->Get("analyze/cutTree");
        //TTree * tree4 = (TTree*) f4->Get("analyze/cutTree");
        //TTree * tree5 = (TTree*) f5->Get("analyze/cutTree");

//        TTree * tree6 = (TTree*) f6->Get("analyze/cutTree");

//        TTree * tree7 = (TTree*) f7->Get("analyze/cutTree");
//        TTree * tree9 = (TTree*) f9->Get("analyze/cutTree");
//        TTree * tree10 = (TTree*) f10->Get("analyze/cutTree");
//        TTree * tree11 = (TTree*) f11->Get("analyze/cutTree");

/*
	tree1->Draw(plot+">>ht1","("+cuts+")");
	tree2->Draw(plot+">>ht2","("+cuts+")");
	tree3->Draw(plot+">>ht3","("+cuts+")");
	tree4->Draw(plot+">>ht4","("+cuts+")");
	tree5->Draw(plot+">>ht5","("+cuts+")");
	tree6->Draw(plot+">>ht6","("+cuts+")");
	tree7->Draw(plot+">>ht7","("+cuts+")");
	tree8->Draw(plot+">>ht8","("+cuts+")");
	tree9->Draw(plot+">>ht9","("+cuts+")");
	tree10->Draw(plot+">>ht10","("+cuts+")");
	tree11->Draw(plot+">>ht11","("+cuts+")");
*/	
	
	cout << "Back Scale: " << sScale << endl;
//	tree1->Draw(plot+">>ht1",sScale+"*("+cuts+")");
	tree2->Draw(plot+">>ht2",sScale+"*("+cuts+")");
	cout << "Plotted TTJets" << endl;
	//tree3->Draw(plot+">>ht3",sScale+"*("+cuts+")");
	//tree4->Draw(plot+">>ht4",sScale+"*("+cuts+")");
	//tree5->Draw(plot+">>ht5",sScale+"*("+cuts+")");
	//tree6->Draw(plot+">>ht6",sScale+"*("+cuts+")");
	tree7->Draw(plot+">>ht7",sScale+"*("+cuts+")");
	cout << "Plotted QCD700" << endl;
	tree8->Draw(plot+">>ht8",sScale+"*("+cuts+")");
	cout << "Plotted QCD1000" << endl;
	tree9->Draw(plot+">>ht9",sScale+"*("+cuts+")");
	cout << "Plotted QCD1500" << endl;
	tree10->Draw(plot+">>ht10",sScale+"*("+cuts+")");
	cout << "Plotted QCD2000" << endl;
	tree11->Draw(plot+">>ht11",sScale+"*("+cuts+")");
	cout << "Plotted WJets" << endl;
	tree12->Draw(plot+">>ht12",sScale+"*("+cuts+")");
	cout << "Plotted ST" << endl;


/*
	tree1->Draw(plot+">>ht1","EvtWeight[0]*("+cuts+")");
	tree2->Draw(plot+">>ht2","EvtWeight[0]*("+cuts+")");
	tree3->Draw(plot+">>ht3","EvtWeight[0]*("+cuts+")");
	tree4->Draw(plot+">>ht4","EvtWeight[0]*("+cuts+")");
	tree5->Draw(plot+">>ht5","EvtWeight[0]*("+cuts+")");
	tree6->Draw(plot+">>ht6","EvtWeight[0]*("+cuts+")");
	tree7->Draw(plot+">>ht7","EvtWeight[0]*("+cuts+")");
	tree8->Draw(plot+">>ht8","EvtWeight[0]*("+cuts+")");
	tree9->Draw(plot+">>ht9","EvtWeight[0]*("+cuts+")");
	tree10->Draw(plot+">>ht10","EvtWeight[0]*("+cuts+")");
	tree11->Draw(plot+">>ht11","EvtWeight[0]*("+cuts+")");
*/
	cout << "data cuts: " << cuts  << endl;
	//TString datacuts(cuts);
        //datacuts = datacuts.ReplaceAll("PUWeight(npuTrue)*","");
	
	treeData->Draw(plot+">>htdata",cuts,"E");
	cout << "Plotted Data" << endl;

	//Dump Events to text file
	//
	
	//treeData->Scan("htak4:mass(ptAK8[HTagIdx[0]],etaAK8[HTagIdx[0]],phiAK8[HTagIdx[0]],MAK8[HTagIdx[0]],ptAK8[TTagIdx03[0]],etaAK8[TTagIdx03[0]],phiAK8[TTagIdx03[0]],MAK8[TTagIdx03[0]]):EvtWeight[0]:EvtWeight[4]/1.21:WeightHT(htak4)","htak4>1000&&@HTagIdx.size()>0&&@TTagIdx03.size()>0&&bTrigger",0,0);
	

	double lumi = 2197  ; //1.929/2 ;//1.28/2;

	std::map<TString , TH1D*> hSignal;
	int c = 0;
	for( std::map<TChain * , TString>::iterator it = fSig.begin() ; it != fSig.end(); it++) {
	//    cout << "Find: " << it->second << "  " ;
	    TH1D * htemp = (TH1D*) gROOT->FindObject(it->second);
	//    cout << htemp << endl ;
	    std::map<TString,TH1D*>::iterator hit = (hSignal.insert(make_pair(it->second+" x "+TString::Itoa(sigScale,10),htemp))).first;
	//    cout << "hit->second: " <<hit->second << endl;
	    hit->second->Scale(1*lumi/nEvts[it->second]*sigScale);			
            hit->second->SetLineColor(kRed+c);
	    c++;
	}

//	cout << "Filled hSignal" << endl;

	//hist1 = (TH1D*) gROOT->FindObject("ht1");
	hist2 = (TH1D*) gROOT->FindObject("ht2")->Clone("TTJets");
	//hist3 = (TH1D*) gROOT->FindObject("ht3");
	//hist4 = (TH1D*) gROOT->FindObject("ht4");
	//hist5 = (TH1D*) gROOT->FindObject("ht5");
	//hist6 = (TH1D*) gROOT->FindObject("ht6");
	hist7 = (TH1D*) gROOT->FindObject("ht7");
	hist8 = (TH1D*) gROOT->FindObject("ht8");
	hist9 = (TH1D*) gROOT->FindObject("ht9");
	hist10 = (TH1D*) gROOT->FindObject("ht10");
	hist11 = (TH1D*) gROOT->FindObject("ht11")->Clone("WJets");
	hist12 = (TH1D*) gROOT->FindObject("ht12")->Clone("ST");
	histData = (TH1D*) gROOT->FindObject("htdata")->Clone("Data");

	cout << "TTJets SF: " << 831.76/nEvts["TTJets"]*lumi << endl;
	cout << "QCD700 SF: " << 6831/nEvts["QCDHT700"]*lumi << endl;
	cout << "QCD700 SF: " << 1207/nEvts["QCDHT1000"]*lumi << endl;

	
        hist2->Scale(831.76/nEvts["TTJets"]*lumi);
        //hist3->Scale(672*lumi);
        //hist4->Scale(186*lumi);
        //hist5->Scale(36*lumi);
        //hist6->Scale(3*lumi);
        hist7->Scale(6831/nEvts["QCDHT700"]*lumi);
        hist8->Scale(1207/nEvts["QCDHT1000"]*lumi);
        hist9->Scale(119.9/nEvts["QCDHT1500"]*lumi);
        hist10->Scale(25.24/nEvts["QCDHT2000"]*lumi);
        hist11->Scale(95.14/nEvts["WJets"]*lumi);
	hist12->Scale(35.6/nEvts["ST"]*lumi);

        hist2->SetFillColor(3);
        //hist3->SetFillColor(4);
	//hist4->SetFillColor(5);
	//hist5->SetFillColor(6);
//	hist6->SetFillColor(7);
	hist7->SetFillColor(8);
	hist8->SetFillColor(9);
	hist9->SetFillColor(10);
	hist10->SetFillColor(11);
	hist11->SetFillColor(12);
	hist12->SetFillColor(13);

	//hs->Add(hist1);
	hs->Add(hist2,"hist");
	hs->Add(hist11,"hist");
	//hs->Add(hist3,"hist");
	//hs->Add(hist4,"hist");
	//hs->Add(hist5,"hist");
	//hs->Add(hist6,"hist");
	hs->Add(hist7,"hist");
	hs->Add(hist8,"hist");
	hs->Add(hist9,"hist");
	hs->Add(hist10,"hist");
	hs->Add(hist12,"hist");

	//hs->SetMaximum(700);

	//TCanvas c1 = new TCanvas("c1");

	
	//hs->SetMaximum(yMax);
	
//        hs->Draw("F");
//	TH1D * stack = (TH1D*) hs->GetHistogram();
//	stack->SetTitle("Cuts: "+cuts);
//	stack->GetXaxis()->SetTitle(label);
	

	//cout << "Signal Events: " << hist1->Integral(0,8000) << endl;
	//cout << "Signal Eff: " << hist1->Integral(0,8000) / (.61 * 2000 * lumi) << endl;

	double csErr[10] = { 	
		0.054, 	// TTJets
		0.026,	//QCD100
		0.030,	//QCD200
		0.034,	//QCD300
		0.037,	//QCD500
		0.053,	//QCD700
		0.056,	//QCD1000
		0.052,	//QCD1500
		0.052,	//QCD2000
		0.038	//WJets
	};

	TH1D * fromStack = (TH1D*)((TH1D*)(hs->GetStack()->Last()))->Clone("hBack");

	fromStack->GetXaxis()->SetTitle(label);	
	fromStack->GetYaxis()->SetTitle(yLabel);	
	fromStack->GetYaxis()->SetTitleSize(0.06);	
	fromStack->GetYaxis()->SetTitleOffset(1);	
	fromStack->SetTitle(title);
/*	
	for ( int i = 0 ; i < fromStack->GetNbinsX() ; i++) {
	//   double statErr = pow(fromStack->GetBinError(i),2);
	//   double csErrTotal = pow(hist2->GetBinContent(i)*csErr[0],2);
	   
	   cout << "Stack Bin: " << i << "  Stat: " << fromStack->GetBinError(i) << " cont: " << fromStack->GetBinContent(i) << endl; 
	   cout << "TT Bin: " << i << "  Stat: " << hist2->GetBinError(i) << " cont: " << hist2->GetBinContent(i) << endl; 
	   cout << "QCD700 Bin: " << i << "  Stat: " << hist7->GetBinError(i) << " cont: " << hist7->GetBinContent(i) << endl; 
	   cout << "QCD1000 Bin: " << i << "  Stat: " << hist8->GetBinError(i) << " cont: " << hist8->GetBinContent(i) << endl; 
	   cout << "QCD1500 Bin: " << i << "  Stat: " << hist9->GetBinError(i) << " cont: " << hist9->GetBinContent(i) << endl; 
	   cout << "QCD2000 Bin: " << i << "  Stat: " << hist10->GetBinError(i) << " cont: " << hist10->GetBinContent(i) << endl; 
	   cout << "W Bin: " << i << "  Stat: " << hist11->GetBinError(i) << " cont: " << hist11->GetBinContent(i) << endl; 
	   cout << "ST Bin: " << i << "  Stat: " << hist12->GetBinError(i) << " cont: " << hist12->GetBinContent(i) << endl; 
	}
	  // csErrTotal += pow(hist3->GetBinContent(i)*csErr[1],2);
	  // csErrTotal += pow(hist4->GetBinContent(i)*csErr[2],2);
	  // csErrTotal += pow(hist5->GetBinContent(i)*csErr[3],2);
	  // csErrTotal += pow(hist6->GetBinContent(i)*csErr[4],2);
	   csErrTotal += pow(hist7->GetBinContent(i)*csErr[5],2);
	   csErrTotal += pow(hist8->GetBinContent(i)*csErr[6],2);
	   csErrTotal += pow(hist9->GetBinContent(i)*csErr[7],2);
	   csErrTotal += pow(hist10->GetBinContent(i)*csErr[8],2);
	   csErrTotal += pow(hist11->GetBinContent(i)*csErr[9],2);
	   fromStack->SetBinError(i,sqrt(statErr+csErrTotal));

	}

	cout << "Total errors: " <<endl;
*/
	double err = 0;
	double integral = hist2->IntegralAndError(0,1000,err);
	cout << "TT: " << integral << " +/- " << err << endl; //  << sqrt(pow(integral*csErr[0],2) + pow(err,2)) << endl;   

//	integral = hist3->IntegralAndError(0,1000,err);
//	cout << "QCD100: "  << integral << " +/- " << sqrt(pow(integral*csErr[1],2) + pow(err,2)) << endl;   

//	integral = hist4->IntegralAndError(0,1000,err);
//	cout << "QCD200: "  << integral << " +/- " << sqrt(pow(integral*csErr[2],2) + pow(err,2)) << endl;   

//	integral = hist5->IntegralAndError(0,1000,err);
//	cout << "QCD300: "  << integral << " +/- " << sqrt(pow(integral*csErr[3],2) + pow(err,2)) << endl;   

//	integral = hist6->IntegralAndError(0,1000,err);
//	cout << "QCD500: "  << integral << " +/- " << sqrt(pow(integral*csErr[4],2) + pow(err,2)) << endl;   

	integral = hist7->IntegralAndError(0,1000,err);
	cout << "QCD700: "  << integral << " +/- " << err << endl;// << sqrt(pow(integral*csErr[5],2) + pow(err,2)) << endl;   

	integral = hist8->IntegralAndError(0,1000,err);
	cout << "QCD1000: "  << integral << " +/- "<< err << endl;// << sqrt(pow(integral*csErr[6],2) + pow(err,2)) << endl;   

	integral = hist9->IntegralAndError(0,1000,err);
	cout << "QCD1500: "  << integral << " +/- " << err << endl;//<< sqrt(pow(integral*csErr[7],2) + pow(err,2)) << endl;   

	integral = hist10->IntegralAndError(0,1000,err);
	cout << "QCD2000: " << integral << " +/- " << err << endl;// << sqrt(pow(integral*csErr[8],2) + pow(err,2)) << endl;   
  
	integral = hist11->IntegralAndError(0,1000,err);
	cout << "WJets: " << integral << " +/- " << err << endl;// << sqrt(pow(integral*csErr[9],2) + pow(err,2)) << endl;   

	integral = hist12->IntegralAndError(0,1000,err);
	cout << "ST: " << integral << " +/- " << err << endl;// << sqrt(pow(integral*csErr[9],2) + pow(err,2)) << endl;   
  

	cout << "Background Events: " << fromStack->Integral(0,1000) << endl; 
//	cout << "Background Eff: " << back/(2317750.0*lumi) << endl;
	
	TString s = ((TObjString *)(sigNames->At(0)))->String();

	double srb = hSignal[s+" x "+TString::Itoa(sigScale,10)]->Integral(0,8000)/sqrt(fromStack->Integral(0,1000));

	cout << "S/sqrt(B): " << srb << endl;


	int data = histData->Integral(0,1000);
	cout << "Data Events: " << data << endl;
	
	//double SF = data/back;
	//cout << "Scale Factor: "<< SF << endl;

	//fromStack->Scale(SF);
	

	THStack * hsQCD = new THStack("hsQCD","QCD");
//	hsQCD->Add(hist3);
//	hsQCD->Add(hist4);
//	hsQCD->Add(hist5);
//	hsQCD->Add(hist6);
	hsQCD->Add(hist7);
	hsQCD->Add(hist8);
	hsQCD->Add(hist9);
	hsQCD->Add(hist10);

	TH1D * histQCD = (TH1D * )((TH1D*)(hsQCD->GetStack()->Last()))->Clone("histQCD");

	integral = histQCD->IntegralAndError(0,1000,err);
        cout << "QCD_Total: " << integral << " +/- "<< err << endl;//  << sqrt(pow(integral*csErr[9],2) + pow(err,2)) << endl;


//	double qcdSF= (histData->Integral(0,1000)-hist11->Integral(0,1000)-hist2->Integral(0,1000))/histQCD->Integral(0,1000);

//	histQCD->Scale(qcdSF);
//

	TFile rFile("out_"+title+".root","RECREATE");
	histData->Write();
	histQCD->Write();
	hist11->Write();
	hist2->Write();
	hist12->Write();
	
	for( std::map<TString,TH1D*>::iterator it = hSignal.begin() ; it != hSignal.end(); it++) {
		cout << "Writing "<< it->first << endl;
		it->second->Write();
	}

	rFile.Close();
	

        TCanvas * c1 = new TCanvas("c1");
        c1->cd();

	if(!bSep) {
	   if(bData)
	      	DrawPlot(c1,fromStack,  histData, hSignal, histQCD ,hist11, hist2, hist12 );
	   else {
		    TH1D* hd = 0;
		    DrawPlot(c1,fromStack,  hd, hSignal ,histQCD ,hist11, hist2 ,hist12);
		}
	}
	else {	
        hs->Draw("F");
//        hist1->Draw("same");

	if(bData) {
		histData->SetLineColor(kBlack);
		//histData->SetMarkerStyle(7);
//		histData->Draw("samePE");
	}
//        hist3->Draw("SAME");
//        hist4->Draw("SAME");

        TLegend * leg = new TLegend(0.6,0.6,0.80,0.85);
//        leg->AddEntry(hist1,"Tprime");
        leg->AddEntry(hist2,"TTJets");
	leg->AddEntry(hist11,"WJets");
	leg->AddEntry(hist12,"SingleTop");
//        leg->AddEntry(hist3,"QCD100");
//        leg->AddEntry(hist4,"QCD200");
//        leg->AddEntry(hist5,"QCD300");
//        leg->AddEntry(hist6,"QCD500");
        leg->AddEntry(hist7,"QCD700");
        leg->AddEntry(hist8,"QCD1000");
        leg->AddEntry(hist9,"QCD1500");
        leg->AddEntry(hist10,"QCD2000");
    //    if (bData ) leg->AddEntry(histData,"2015D-1920");
        leg->Draw();
	//ratioPlot(c1, hs, histData);

	}
	
	return 0;
}

void ratioPlot(TCanvas * c1 , THStack * hs , TH1D * hDataD)
{

      TH1D * fromStack = ((TH1D*)(hs->GetStack()->Last()));
      ratioPlot(c1, fromStack , hDataD);

}

void ratioPlot(TCanvas * c1 , TH1D * fromStack , TH1D * hDataD)
{
    //Make Little Comparison Plot Below                                                                                                        
      c1->cd();
      TPad *pad2 = new TPad("pad2","pad2",0,0,1,.2);
      pad2->SetBottomMargin(0.18);
      pad2->SetTopMargin(0.06);
      pad2->Draw();
      pad2->cd();


      //pad2->SetLogy();                                                                                                                         

      //TH1D * ratio = (TH1D*) hDataD->Clone("ratio");
      TGraphErrors * ratio = new TGraphErrors(); 
//      pad2->cd();
      //pad2->SetLogy();                                                                                                                         
      int lx[2] = {0, 100000};
      int ly[2] = {0, 0};
      TGraph* zeroline = new TGraph(2, lx, ly);
      zeroline->SetLineColor(kGray+2);

//      fromStack = ((TH1D*)(hs->GetStack()->Last()));


     for(int i = 0; i<=fromStack->GetXaxis()->GetNbins(); i++)
        {
	  if( fromStack->GetBinContent(i) > 0 ) {
		double x = fromStack->GetXaxis()->GetBinCenter(i);
		double y = hDataD->GetBinContent(i)/fromStack->GetBinContent(i)-1;

		double xe = fromStack->GetXaxis()->GetBinCenter(i)-fromStack->GetXaxis()->GetBinLowEdge(i);
	  	double ye = hDataD->GetBinContent(i)/fromStack->GetBinContent(i)*sqrt(pow(hDataD->GetBinError(i)/hDataD->GetBinContent(i),2)+pow(fromStack->GetBinError(i)/fromStack->GetBinContent(i),2));


		ratio->SetPoint(i,x,y);
		ratio->SetPointError(i,xe,ye);
	  }
	}
/*
	gStyle->SetOptFit(1111);

	TF1 * func = new TF1("func","[0]+x*[1]");
	ratio->Fit("func","L","",1000,2400);
	TF1 *fit = ratio->GetFunction("func");
	
	cout << "Chi2: "<< fit->GetChisquare() << endl;
	cout << "Par0: " << fit->GetParameter(0) << "+/-" << fit->GetParError(0) << endl;
	cout << "Par1: " << fit->GetParameter(1) << "+/-" << fit->GetParError(1) << endl;

	TH1D * th = (TH1D*) fit->GetHistogram();
	cout << "Mean: " << th->GetMean() << endl;;
*/	
	
/*
          if(fromStack->GetBinContent(i) < 1 && (fromStack->GetBinContent(i) == 0 || ratio->GetBinContent(i) == 0))
            {
              fromStack->SetBinContent(i,0);
            }
        }

      ratio->Add(fromStack, -1);
      for(int i = 0; i<fromStack->GetXaxis()->GetNbins(); i++)
        {
          if(fromStack->GetBinContent(i) == 0 || fromStack->GetBinContent(i) < 1)
            {
              fromStack->SetBinContent(i,1);
            }
	}
      ratio->Divide(fromStack);


      for(int i = 0; i<fromStack->GetXaxis()->GetNbins(); i++)
        {
 
	  double error = hDataD->GetBinContent(i)/fromStack->GetBinContent(i)*sqrt(pow(hDataD->GetBinError(i)/hDataD->GetBinContent(i),2)+pow(fromStack->GetBinError(i)/fromStack->GetBinContent(i),2));


	  ratio->SetBinError(i,error);	
//          fromStack->SetBinError(i, (sqrt( (sqrt(hDataD->GetBinContent(i)/fromStack->GetBinContent(i)) * sqrt(hDataD->GetBinContent(i)/fromStack\
->GetBinContent(i)) ) + ((hDataD->GetBinContent(i)/fromStack->GetBinContent(i)) * ey[i]/fromStack->GetBinContent(i))*(hDataD->GetBinContent(i)/f\
romStack->GetBinContent(i)) * ey[i]/fromStack->GetBinContent(i))));
        }
*/

      ratio->Draw("AP");
      //ratio->GetXaxis()->SetRangeUser(fromStack->GetXaxis()->GetXmin(), fromStack->GetXaxis()->GetXmax());
      ratio->GetXaxis()->SetLimits(fromStack->GetXaxis()->GetXmin(), fromStack->GetXaxis()->GetXmax());
      ratio->SetMinimum(-1);
      ratio->SetMaximum(1);
      TAxis * ya = ratio->GetYaxis();
      if (ya) {
	ya->SetTitle("#frac{Data - MC}{MC}");
	ya->SetTitleSize(.1);
	ya->SetTitleOffset(.4);

      }
      else
	cout << " no y axis" << endl;

      ratio->GetXaxis()->SetLabelFont(63); //font in pixels                                                                                      
      ratio->GetXaxis()->SetLabelSize(16); //in pixels                                                                                           
      ratio->GetYaxis()->SetLabelFont(63); //font in pixels                                                                                      
      ratio->GetYaxis()->SetLabelSize(10); //in pixels                                                         
      ratio->GetXaxis()->SetTitleFont(63);
      ratio->GetXaxis()->SetTitleSize(16);
      //ratio->GetYaxis()->SetTitleSize(5);
      ratio->GetXaxis()->SetTitleOffset(3);
	ratio->SetTitle("");

      zeroline->Draw("lsame");
/*
	TFile * rfile = new TFile("ratio.root","RECREATE");

	pad2->Write();
	
	rfile->Close();
*/

} 



void ABCDData(bool bMt, int HTscale = 0, int btagSF = 0, int ttagSF = 0 ,int LHEweight = 0, TString sOpt = "Nominal")//TString plot, TString cutA, TString cutB, TString cutC, TString cutD)
{

	TString sExt;

	if(sOpt.BeginsWith("_JE")) 
		sExt = sOpt;

        TString lumiText = "2.2 fb^{-1} (13 TeV)";
        TString cmsText = "#bf{CMS}";
        TString extraText = "Preliminary";

        TLatex latex;
        latex.SetNDC();
        latex.SetTextAngle(0);
        latex.SetTextColor(kBlack);

        latex.SetTextFont(42);
        latex.SetTextAlign(31);
        latex.SetTextSize(.04);

	//TString sScale = "WtTrig(ht)*EvtWeight*EvtWtPV";
	TString sScale = "EvtWeight*EvtWtPV";
        //TString sScale = "WeightHT(ht)*EvtWeight*EvtWtPV";
	//sScale += "*EvtWtHT";
	
//	if(HTscale == 1) sScale += "Up";
//	else if (HTscale == -1)  sScale += "Down";
	
	sScale += "*btagsf";	

	if(btagSF == 1) sScale += "_bcUp";
	else if (btagSF == -1)  sScale += "_bcDown";
	
	if(btagSF == 2) sScale += "_lUp";
	else if (btagSF == -2)  sScale += "_lDown";
	

	TString tScale = "" ;
	if(ttagSF == 0 ) tScale = "*topSF(ptTopTagged)";
	if(ttagSF == 1)  tScale = "*topSFUp(ptTopTagged)";
	if(ttagSF == -1)  tScale = "*topSFDown(ptTopTagged)";

        TString str_LHEweight;
        str_LHEweight.Form("%i",LHEweight); 
	TString cuts = "ht>1100&&" ;
	if(LHEweight > 0){
		sScale += "*lhewts.second";
		cuts += "lhewts.first=="+str_LHEweight+"&&"; 
	}

	makeStack("ht", cuts+"isRegionA" ,"Tprime1200_LH","HT GeV","Events","Cut A",1,2,40,1000,2600,sScale,false,false,sExt);


        TH1D * histA = (TH1D*) gROOT->FindObject("htdata")->Clone();
        TH1D * histAQCD = (TH1D*) gROOT->FindObject("histQCD")->Clone();
	TH1D * histATT = (TH1D*) gROOT->FindObject("TTJets")->Clone();
	TH1D * histAW = (TH1D*) gROOT->FindObject("WJets")->Clone();
	TH1D * histAST = (TH1D*) gROOT->FindObject("ST")->Clone();

	//delete gROOT->FindObject("TTJets");

        //cout << "TT A: " << histATT->Integral(0,1000) << endl;


        TCanvas * c1 = (TCanvas * ) gROOT->FindObject("c1");
        c1->Print("CutAdata.pdf");
	if(bMt) 
		makeStack("mtprimeDummy", cuts+"isRegionB","Tprime1200_LH","HT GeV","Events","Cut B",1,1,36,600,2400,sScale+tScale,false,false,sExt);
	else
        	makeStack("ht",cuts+"isRegionB","Tprime1200_LH","HT GeV","Events","Cut B",1,2,40,1000,2600,sScale+tScale,false,false,sExt);


        TH1D * histB = (TH1D*) gROOT->FindObject("htdata")->Clone();
        TH1D * histBQCD = (TH1D*) gROOT->FindObject("histQCD")->Clone();
	TH1D * histBTT = (TH1D*) gROOT->FindObject("TTJets")->Clone();
	TH1D * histBW = (TH1D*) gROOT->FindObject("WJets")->Clone();
	TH1D * histBST = (TH1D*) gROOT->FindObject("ST")->Clone();

        //cout << "TT A: " << histATT->Integral(0,1000) << endl;


        c1 = (TCanvas * ) gROOT->FindObject("c1");
        c1->Print("CutBdata.pdf");

	

        makeStack("ht", cuts+"isRegionC","Tprime1200_LH","HT GeV","Events","Cut C",1,2,40,1000,2600,sScale,false,false,sExt);
        TH1D * histC = (TH1D*) gROOT->FindObject("htdata")->Clone();
        TH1D * histCQCD = (TH1D*) gROOT->FindObject("histQCD")->Clone();
	TH1D * histCTT = (TH1D*) gROOT->FindObject("TTJets")->Clone();
	TH1D * histCW = (TH1D*) gROOT->FindObject("WJets")->Clone();
	TH1D * histCST = (TH1D*) gROOT->FindObject("ST")->Clone();

        //cout << "TT A: " << histATT->Integral(0,1000) << endl;

        c1 = (TCanvas * ) gROOT->FindObject("c1");
        c1->Print("CutCdata.pdf");

        if (bMt) makeStack("mtprime", cuts+"isRegionD","Tprime1200_LH","HT GeV","Events","Cut D",1,1,36,600,2400,sScale+tScale,false,false,sExt);
	else
        	makeStack("ht", cuts+"isRegionD","Tprime1200_LH","HT GeV","Events","Cut D",1,2,40,1000,2600,sScale+tScale,false,false,sExt);

        //cout << "TT A: " << histATT->Integral(0,1000) << endl;


	TH1D * hdata = (TH1D*) gROOT->FindObject("htdata");
        TH1D * histD = (TH1D*) gROOT->FindObject("htdata")->Clone();
        TH1D * histDQCD = (TH1D*) gROOT->FindObject("histQCD")->Clone();
	TH1D * histDTT = (TH1D*) gROOT->FindObject("TTJets")->Clone();
	TH1D * histDW = (TH1D*) gROOT->FindObject("WJets")->Clone();
	TH1D * histDST = (TH1D*) gROOT->FindObject("ST")->Clone();
	TH1D * histDBack= (TH1D*) gROOT->FindObject("hBack")->Clone();

	cout << "TT A: " << histATT->Integral(0,1000) << endl;
        cout << "TT B: " << histBTT->Integral(0,1000) << endl;
        cout << "TT C: " << histCTT->Integral(0,1000) << endl;
        cout << "TT D: " << histDTT->Integral(0,1000) << endl;

	cout << "ST A: " << histAST->Integral(0,1000) << endl;
        cout << "ST B: " << histBST->Integral(0,1000) << endl;
        cout << "ST C: " << histCST->Integral(0,1000) << endl;
        cout << "ST D: " << histDST->Integral(0,1000) << endl;

        cout << "W A: " << histAW->Integral(0,1000) << endl;
        cout << "W B: " << histBW->Integral(0,1000) << endl;
        cout << "W C: " << histCW->Integral(0,1000) << endl;
        cout << "W D: " << histDW->Integral(0,1000) << endl;

	cout << "Data A: " << histA->Integral(0,1000) << endl;
        cout << "Data B: " << histB->Integral(0,1000) << endl;
        cout << "Data C: " << histC->Integral(0,1000) << endl;
        cout << "Data D: " << histD->Integral(0,1000) << endl;


	//Data

        histA->Add(histATT,-1);
        histA->Add(histAW,-1);
        histA->Add(histAST,-1);

        histB->Add(histBTT,-1);
        histB->Add(histBW,-1);
        histB->Add(histBST,-1);

        histC->Add(histCTT,-1);
        histC->Add(histCW,-1);
        histC->Add(histCST,-1);

        histD->Add(histDTT,-1);
        histD->Add(histDW,-1);
        histD->Add(histDST,-1);

	//MC

        cout << "DataQCD A: " << histA->Integral(0,1000) << endl;
        cout << "DataQCD B: " << histB->Integral(0,1000) << endl;
        cout << "DataQCD C: " << histC->Integral(0,1000) << endl;
        cout << "DataQCD D: " << histD->Integral(0,1000) << endl;


        c1 = new TCanvas("c2");

        c1->cd();

        //D=C*B/A -> A/B = C/D 
        double SF = histA->Integral(0,1000)/histB->Integral(0,1000)/histC->Integral(0,1000) * histD->Integral(0,1000);
        cout << "A: " << histA->Integral(0,1000) << endl;
        cout << "B: " << histB->Integral(0,1000) << endl;
        cout << "C: " << histC->Integral(0,1000) << endl;
        cout << "D: " << histD->Integral(0,1000) << endl;
        cout << "SF: " << SF << endl;
        cout << "A/B: " << histA->Integral(0,1000)/histB->Integral(0,1000) << endl;
        cout << "C/D: " << histC->Integral(0,1000)/histD->Integral(0,1000) << endl;
///
//	Data BD Comparison Plots
//



        TH1D * histShapeBMC = (TH1D *) histBQCD->Clone();
        TH1D * histShapeDMC = (TH1D *) histDQCD->Clone();

        TH1D * histShapeB = (TH1D *) histB->Clone();
        TH1D * histShapeD = (TH1D *) histD->Clone();

        histShapeBMC->Scale(1/histShapeB->Integral(0,1000));
        histShapeDMC->Scale(1/histShapeD->Integral(0,1000));

        histShapeDMC->SetLineColor(kRed);
        histShapeDMC->SetMarkerColor(kRed);
	histShapeDMC->SetLineStyle(2);
	histShapeBMC->SetLineStyle(1);
	histShapeDMC->SetFillColor(0);
	histShapeBMC->SetFillColor(0);

	histShapeBMC->SetFillStyle(0);
	histShapeDMC->SetFillStyle(0);

	if(bMt)
	    histShapeDMC->GetXaxis()->SetTitle("m_{T} GeV");
	else
	    histShapeDMC->GetXaxis()->SetTitle("H_{T} GeV");

	histShapeDMC->GetYaxis()->SetTitle("a.u.");
	
        histShapeDMC->Draw("hist");
        histShapeBMC->Draw("hist Same");

	
	if(bMt)
		cout << "Mt:" << endl;
	else
		cout << "Ht: " <<endl;

        cout << "Data BD KSTest: " << histShapeB->KolmogorovTest(histShapeD) << endl;
        cout << "MC BD KSTest: " << histShapeBMC->KolmogorovTest(histShapeDMC) << endl;




        double x0,x1;

        // Find best position for Legend.

        if(histShapeBMC->GetMaximumBin() > histShapeBMC->GetXaxis()->GetNbins() * .4){
                x0 = .2;
                x1 = .4;
        }
        else {
                x0 = 0.6;
                x1 = 0.8;
        }
 //       ratioPlot(c1, histShapeBMC, histShapeDMC);

	  	

        TH1D * Dest = (TH1D*) histB->Clone("Dest");
 	TH1D * DestMC = (TH1D*) histBQCD->Clone("DestMC");	


 

        Dest->Scale(histC->Integral(0,1000)/histA->Integral(0,1000));
        DestMC->Scale(histCQCD->Integral(0,1000)/histAQCD->Integral(0,1000));


	if(!bMt) {
		TFile limithists("LimitHists-HT"+sOpt+".root","RECREATE");
	
		Dest->Write("QCD-Est");
		histDTT->Write("TT-MC");
		histDW->Write("W-MC");
		histDST->Write("ST-MC");
		hdata->Write("data_obs");
		limithists.Close();
	}
	else {
		TFile limithists("LimitHists-MT"+sOpt+".root","RECREATE");
	
		Dest->Write("QCD-Est");
		histDTT->Write("TT-MC");
		histDW->Write("W-MC");
		histDST->Write("ST-MC");
		hdata->Write("data_obs");
		limithists.Close();
	}
/*
	TH1D * hCombEst = (TH1D *) Dest->Clone("hCombEst");
	hCombEst->Add(histDTT);
	hCombEst->Add(histDW);
 
	TCanvas * c1Est = new TCanvas("c2");

        c1Est->cd();

	std::map<TH1D*,TString> hSignal;
	
	DrawPlot(c1Est, hCombEst, 0, hSignal, Dest ,histDW, histDTT );

	c1Est->SaveAs("EstBack.pdf");

        Dest->Add(histDTT);
        Dest->Add(histDW);

        histD->Add(histDTT);
        histD->Add(histDW);

	DestMC->Add(histDTT);
	DestMC->Add(histDW);


	



	//Add data to B/D MC plot
	//TH1D * DestNorm = (TH1D *) Dest->Clone("DestNorm");

	//DestNorm->Scale(1/DestNorm->Integral(0,1000));
	
	//DestNorm->Draw("same");

        TLegend * leg = new TLegend(x0,0.6,x1,0.85);

        leg->AddEntry(histShapeBMC,"MC Sideband Region B");
        leg->AddEntry(histShapeDMC,"Signal Region D");
	leg->AddEntry(Dest,"Data-Driven Est.");

        leg->Draw();

	TH1D * histShapeBMCerr = (TH1D*) histShapeBMC->Clone("BMCerr");
	TH1D * histShapeDMCerr = (TH1D*) histShapeDMC->Clone("DMCerr");

        histShapeDMCerr->SetMarkerStyle(0);
        histShapeDMCerr->SetFillColor(kRed+2);
        histShapeDMCerr->SetFillStyle(3017);
        histShapeDMCerr->Draw("e2same");

        histShapeBMCerr->SetMarkerStyle(0);
        histShapeBMCerr->SetFillColor(kGray+2);
        histShapeBMCerr->SetFillStyle(3018);
        histShapeBMCerr->Draw("e2same");



        latex.DrawLatex(.8,.96,lumiText);
        latex.DrawLatex(x0,.89,cmsText);
        latex.DrawLatex(x1,.86,extraText);


	if(bMt)
        	c1->Print("mtregbdvsmc.pdf");
	else
        	c1->Print("htregbdvsmc.pdf");

	//Draw Data
	//
	
        c1 = new TCanvas("c3");
        c1->cd();

        TPad *pad2 = new TPad("pad4","pad1",0,0.3,1,1);
        pad2->SetBottomMargin(0.08);
        pad2->SetTopMargin(0.05);
        pad2->Draw();
        pad2->cd();

        Dest->Draw();
        histDBack->SetLineColor(kRed);
        histDBack->SetMarkerColor(kRed);
        histDBack->Draw("same");


        // Find best position for Legend.

        if(Dest->GetMaximumBin() > Dest->GetXaxis()->GetNbins() * .4){
                x0 = .2;
                x1 = .4;
        }
        else {
                x0 = 0.6;
                x1 = 0.8;
        }
        leg = new TLegend(x0,0.6,x1,0.85);

        leg->AddEntry(Dest,"Est. Back from data");
        leg->AddEntry(histDBack,"Sim. Signal Region");


        leg->Draw();

            ratioPlot(c1, Dest, histDBack);
	
	if( bMt )
		c1->Print("ABCDEst-Mt.pdf");
	else
		c1->Print("ABCDEst-Ht.pdf");

	//Draw MC

        c1 = new TCanvas("c4");
        c1->cd();

        pad2 = new TPad("pad5","pad1",0,0.3,1,1);
        pad2->SetBottomMargin(0.08);
        pad2->SetTopMargin(0.05);
        pad2->Draw();
        pad2->cd();

        DestMC->Draw();
        histDBack->SetLineColor(kRed);
        histDBack->SetMarkerColor(kRed);
        histDBack->Draw("same");


        // Find best position for Legend.

        if(Dest->GetMaximumBin() > Dest->GetXaxis()->GetNbins() * .4){
                x0 = .2;
                x1 = .4;
        }
        else {
                x0 = 0.6;
                x1 = 0.8;
        }
        leg = new TLegend(x0,0.6,x1,0.85);

        leg->AddEntry(Dest,"Est. Back from MC");
        leg->AddEntry(histDBack,"Sim. Signal Region");

        leg->Draw();

            ratioPlot(c1, DestMC, histDBack);

	if(bMt){
        	c1->Print("ABCDEstMC-Mt.pdf");
	        cout << "MC_MT KSTest: " << DestMC->KolmogorovTest(histDBack) << endl;
	}
	else {
        	c1->Print("ABCDEstMC-Ht.pdf");
	        cout << "MC_HT KSTest: " << DestMC->KolmogorovTest(histDBack) << endl;
	}
*/

}


void CutFlow(TString plot,TString Signal)
{
	THStack * cutflow = new THStack("hCuts","CutFlow");
	TH1D * histQCD = new TH1D("hQCDflow","QCD Flow",4,0,4);
	TH1D * histTT = new TH1D("hTTflow","TT Flow",4,0,4);
	TH1D * histW = new TH1D("hWflow","W Flow",4,0,4);
	TH1D * histSig = new TH1D("histSig","Sig Flow",4,0,4);
	
        makeStack(plot, "htak4>0",Signal,"HT GeV","Events/50 GeV", "Presel",1,1,40,0,2000,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");
	
	TH1D * histP = (TH1D*) gROOT->FindObject("histQCD")->Clone();
        TH1D * histPTT = (TH1D*) gROOT->FindObject("ht2")->Clone();
        TH1D * histPW = (TH1D*) gROOT->FindObject("ht11")->Clone();
        TH1D * histPSig = (TH1D*) gROOT->FindObject(Signal)->Clone();

        histQCD->SetBinContent(1,histP->Integral(0,1000));
        cout << "QCDP: "<< histP->Integral(0,1000) << endl;

        histTT->SetBinContent(1,histPTT->Integral(0,1000));
        cout << "TTP: "<< histPTT->Integral(0,1000) << endl;

        histW->SetBinContent(1,histPW->Integral(0,1000));
        cout << "WP: "<< histPW->Integral(0,1000) << endl;

	histSig->SetBinContent(1,histPSig->Integral(0,1000));
	cout << "Sig1: "<< histPSig->Integral(0,1000) << endl;

        makeStack(plot, "htak4>1000",Signal,"HT GeV","Events/50 GeV","HT900",1,1,40,0,2000,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");

        TH1D * histA = (TH1D*) gROOT->FindObject("histQCD")->Clone();
        TH1D * histATT = (TH1D*) gROOT->FindObject("ht2")->Clone();
        TH1D * histAW = (TH1D*) gROOT->FindObject("ht11")->Clone();
        TH1D * histASig = (TH1D*) gROOT->FindObject(Signal)->Clone();

	histQCD->SetBinContent(2,histA->Integral(0,1000));
	cout << "QCD1: "<< histA->Integral(0,1000) << endl;

	histTT->SetBinContent(2,histATT->Integral(0,1000));
	cout << "TT1: "<< histATT->Integral(0,1000) << endl;

	histW->SetBinContent(2,histAW->Integral(0,1000));
	cout << "W1: "<< histAW->Integral(0,1000) << endl;

	histSig->SetBinContent(2,histASig->Integral(0,1000));
	cout << "Sig1: "<< histASig->Integral(0,1000) << endl;

        makeStack(plot, "htak4>1000&&@HTagIdx.size()>0",Signal,"HT (GeV)","Events/50 GeV","HTag",1,1,40,0,2000,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");

        TH1D * histB = (TH1D*) gROOT->FindObject("histQCD")->Clone();
        TH1D * histBTT = (TH1D*) gROOT->FindObject("ht2")->Clone();
        TH1D * histBW = (TH1D*) gROOT->FindObject("ht11")->Clone();
        TH1D * histBSig = (TH1D*) gROOT->FindObject(Signal)->Clone();

        histQCD->SetBinContent(3,histB->Integral(0,1000));
	cout << "QCD2: "<< histB->Integral(0,1000) << endl;

        histTT->SetBinContent(3,histBTT->Integral(0,1000));
	cout << "TT2: "<< histBTT->Integral(0,1000) << endl;

        histW->SetBinContent(3,histBW->Integral(0,1000));
	cout << "W2: "<< histBW->Integral(0,1000) << endl;

	histSig->SetBinContent(3,histBSig->Integral(0,1000));
	cout << "Sig2: "<< histBSig->Integral(0,1000) << endl;

        makeStack(plot, "htak4>1000&&@HTagIdx.size()>0&&@TTagIdx03.size()>0",Signal,"HT GeV","Events/50 GeV","TTag",1,1,40,0,2000,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");

        TH1D * histC = (TH1D*) gROOT->FindObject("histQCD")->Clone();
        TH1D * histCTT = (TH1D*) gROOT->FindObject("ht2")->Clone();
        TH1D * histCW = (TH1D*) gROOT->FindObject("ht11")->Clone();
        TH1D * histCSig = (TH1D*) gROOT->FindObject(Signal)->Clone();

        histQCD->SetBinContent(4,histC->Integral(0,1000));
	cout << "QCD3: "<< histC->Integral(0,1000) << endl;

        histTT->SetBinContent(4,histCTT->Integral(0,1000));
	cout << "TT3: "<< histCTT->Integral(0,1000) << endl;

        histW->SetBinContent(4,histCW->Integral(0,1000));
	cout << "W3: "<< histCW->Integral(0,1000) << endl;

	histSig->SetBinContent(4,histCSig->Integral(0,1000));
	cout << "Sig3: "<< histCSig->Integral(0,1000) << endl;
/*
        makeStack(plot, "htak4>1000&&@HTagIdx.size()>0&&@TTagIdx03.size()>0&&fMaxEtaAK4>2",Signal,"HT GeV","Events/50 GeV","FJet",1,1,40,0,2000,"EvtWeight[0]*EvtWeight[4]/1.21*WeightHT(htak4)");

        TH1D * histD = (TH1D*) gROOT->FindObject("histQCD")->Clone();
        TH1D * histDTT = (TH1D*) gROOT->FindObject("ht2")->Clone();
        TH1D * histDW = (TH1D*) gROOT->FindObject("ht11")->Clone();
        TH1D * histDSig = (TH1D*) gROOT->FindObject(Signal)->Clone();

        histQCD->SetBinContent(5,histD->Integral(0,1000));
	cout << "QCD4: "<< histD->Integral(0,1000) << endl;

        histTT->SetBinContent(5,histDTT->Integral(0,1000));
	cout << "TT4: "<< histDTT->Integral(0,1000) << endl;

        histW->SetBinContent(5,histDW->Integral(0,1000));
	cout << "W4: "<< histDW->Integral(0,1000) << endl;

	histSig->SetBinContent(5,histDSig->Integral(0,1000));
	cout << "Sig4: "<< histDSig->Integral(0,1000) << endl;

*/	

        histQCD->SetFillColor(kCyan);
        histW->SetFillColor(kGreen);
        histTT->SetFillColor(kBlue);
	histSig->SetLineColor(kRed);
	
	histQCD->SetMarkerStyle(0);
	histW->SetMarkerStyle(0);
	histTT->SetMarkerStyle(0);
	histSig->SetMarkerStyle(0);


	cutflow->Add(histW);
	cutflow->Add(histTT);
	cutflow->Add(histQCD);


	TCanvas * c2  = new TCanvas("c2");
	c2->cd();

	
    	cutflow->Draw("histF");

	histSig->Draw("Same");

	cutflow->GetXaxis()->SetBinLabel(1,"Presel");
	cutflow->GetXaxis()->SetBinLabel(2,"HT1000");
	cutflow->GetXaxis()->SetBinLabel(3,"HTag");
	cutflow->GetXaxis()->SetBinLabel(4,"TTag");
	//cutflow->GetXaxis()->SetBinLabel(5,"ForwardJet");	

        TLegend * leg = new TLegend(0.6,0.6,0.80,0.85);
        leg->AddEntry(histW,"WJets");
        leg->AddEntry(histTT,"TTJets");
        leg->AddEntry(histQCD,"QCD");
	leg->AddEntry(histSig,Signal);

	leg->Draw("same");
  
}

void Compare(TString plot, TString cut1 ,TString cut2, TString datasets, TString label, TString yLabel, TString title, int rebin, int bins, int xMin, int xMax) 
{
	TObjArray * dsNames = datasets.Tokenize(TString(";"));
	std::vector<TString> datas; 
	TString signals;

	for (Int_t i = 0; i < dsNames->GetEntries(); i++) {

		TString s = ((TObjString *)(dsNames->At(i)))->String();
	        if( s.BeginsWith("Tprime") )
			signals += s + ";";
		else
			datas.push_back(s);	
	}
	

	makeStack(plot, cut1 , signals, label , yLabel, title, 1, rebin, bins, xMin, xMax, "EvtWeight[0]*EvtWeight[4]/1.21");
	
	TH1D * hist;
	
		//hist = gROOT->FindObject(s);
		
	//}

//	makeStack(plot, cut2 , label , yLabel, title, 1, rebin, bins, xMin, xMax, "EvtWeight[0]*EvtWeight[4]/1.21");

	
	

}
