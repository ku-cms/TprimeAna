#include "DataFormats/Math/interface/deltaR.h"
void weightFunctions(){
                   std::cout << "Weighting functions loaded." << endl;
                   return;
}

double mtprimeTilde(double mt, double Mtop, double MHiggs)
{

     return mt - Mtop - MHiggs + 125 + 172.5;
}
double topSFVal(double pT, int shift)
{


     if (pT >= 400) {  //0.1% working point
     if(shift == 0) return 1.03;
     if(shift == 1) return 1.09;
     if(shift == -1) return 0.99;
     }
//   if( pT >= 400) { //0.3% Working point
//        if(shift == 0) return 1.07;
//        if(shift == 1) return 1.12;
//        if(shift == -1) return 1.04;
//     }
//   if( pT >= 400) { //1.0% working point
//        if(shift == 0) return 1.06;
//        if(shift == 1) return 1.14;
//        if(shift == -1) return 1.02;
//     }
//   if( pT >= 400) { //3.0% working point
//        if(shift == 0) return 1.06;
//        if(shift == 1) return 1.15;
//        if(shift == -1) return 1.02;
//     }
        return 1;
}
double topSF(double pT)
{
        return topSFVal(pT, 0);
}
double topSFUp(double pT)
{
        return topSFVal(pT, 1);
}
double topSFDown(double pT)
{
        return topSFVal(pT, -1);
}

double WeightSumPt(double Pt1, double Pt2, int shift)
{
        double SPt = Pt1 + Pt2;
        double wt = 8.38664e-1 * TMath::Exp(-6.05027e-4*SPt) + 5.54459e-1; 
        double sigErr = 1;  
                                                                                                       //Sqrt(sigma(b)^2 + sigma(m)^2*x^2 + 2*x*cov(m,b))
        if(SPt < 850 || SPt > 4000)
                return 1;

        return wt + (shift*sigErr) ; 

}
double WeightHT(double HT, int shift)
{

        double wt = (1+((-0.00018784)*HT + 0.2274));
        double sigErr = TMath::Sqrt(0.000079 + (4.6073/100000000000*HT*HT) + (2*HT*-5.878/100000000)); //with b as intercept and m as slope 
                                                                                                       //Sqrt(sigma(b)^2 + sigma(m)^2*x^2 + 2*x*cov(m,b))
//        double wt = (1+((-0.000142726)*HT + 0.19121));
        //double sigErr = TMath::Sqrt(0.000008189 + (3.9397/1000000000000*HT*HT) + (2*HT*-5.7279/1000000000));
        if(HT < 1100 || HT > 2700)
                return 1;

        return wt + (shift*sigErr) ; 

}
double QuadWeightHT(double HT, int shift)
{

//        double wt = (1+((-0.00018784)*HT + 0.2274));
        double sigErr = TMath::Sqrt(2.96072e-9*2.96072e-9*HT*HT*HT*HT
                                  + 1.07286e-5*1.07286e-5*HT*HT 
                                  + 0.00921116*0.00921116
                                  + 2*HT*HT*HT*-3.1426e-14
                                  + 2*HT*HT*2.6219e-11
                                  + 2*HT*-9.7824e-8 );
        double wt = 3.82408e-8*HT*HT + -2.71605e-4*HT + 1.29308;
        //double sigErr = TMath::Sqrt(0.000008189 + (3.9397/1000000000000*HT*HT) + (2*HT*-5.7279/1000000000));
        if(HT < 1100 || HT > 3200)
                return 1;

        return wt + (shift*sigErr) ; 

}
//double trigWtHT ( double HT, int shift)
//{
//    double bgLumi = 27954.778;
//    double hLumi = 8857.034;
//    double lumi = 36811.812;
//
//
//    double wt = bglumi / lumi * bgEff + hLumi / lumi * hEff;
//    double err = TMath::Sqrt( pow(bgErr*bgLumi/lumi,2) + pow(hErr*hLumi/lumi,2));
//
//    return wt + (shift * err);
//}

double dR(double eta1,double phi1, double eta2, double phi2) {

        return deltaR(eta1,phi1,eta2,phi2);
}
double dEta(double etaTopTagged, double etaHTagged )
{
 

 	return ( etaTopTagged - etaHTagged );

}

double delPhi(double ptTopTagged, double etaTopTagged, double phiTopTagged, double MTopTagged, double ptHTagged, double etaHTagged, double phiHTagged, double MHTagged)
{

        TLorentzVector TCand, HCand;

                TCand.SetPtEtaPhiM(ptTopTagged,
                         etaTopTagged,
                         phiTopTagged,
                         MTopTagged);

                HCand.SetPtEtaPhiM(ptHTagged,
                         etaHTagged,
                         phiHTagged,
                         MHTagged);

        return TCand.DeltaPhi( HCand );

}
//TString Mjj(Int_t idx1, Int_t idx2){
 //   TString out;
//    out.Form("mass(ptAK8[idxAK8[%d]],etaAK8[idxAK8[%d]],phiAK8[idxAK8[%d]],MAK8[idxAK8[%d]],ptAK8[idxAK8[%d]],etaAK8[idxAK8[%d]],phiAK8[idxAK8[%d]],MAK8[idxAK8[%d]])",idx1,idx1,idx1,idx1,idx2,idx2,idx2,idx2);
//    return out;
//}

double Mjj(double pt1, double eta1, double phi1, double M1, double pt2, double eta2, double phi2, double M2){
    TLorentzVector V1, V2;
    V1.SetPtEtaPhiM(pt1,eta1,phi1,M1);
    V2.SetPtEtaPhiM(pt2,eta2,phi2,M2);
    return (V1+V2).M();
}
double pTjj(double pt1, double eta1, double phi1, double M1, double pt2, double eta2, double phi2, double M2){
    TLorentzVector V1, V2;
    V1.SetPtEtaPhiM(pt1,eta1,phi1,M1);
    V2.SetPtEtaPhiM(pt2,eta2,phi2,M2);
    return (V1+V2).Pt();
}
double costheta(double ptTopTagged, double etaTopTagged, double phiTopTagged, double MTopTagged, double ptHTagged, double etaHTagged, double phiHTagged, double MHTagged)
{

	 TLorentzVector TCand, HCand, CCand, TCand_cms, HCand_cms, CCand_cms;
	 TVector3 CCand_Boost;
	 double rapH,thetaH, rapC, thetaC, theta;

                TCand.SetPtEtaPhiM(ptTopTagged,
                         etaTopTagged,
                         phiTopTagged,
                         MTopTagged);

                HCand.SetPtEtaPhiM(ptHTagged,
                         etaHTagged,
                         phiHTagged,
                         MHTagged);
	
		CCand = TCand + HCand;

		CCand_Boost  = CCand.BoostVector();
   		//TCand_cms = TCand;
   		//TCand_cms.Boost( -1 * CCand_Boost);
                HCand_cms = HCand;
                HCand_cms.Boost( -1 * CCand_Boost);
                //CCand_cms = CCand;
                //CCand_cms.Boost( -1 * CCand_Boost);            	

/*		rapH = HCand_cms.PseudoRapidity();
		thetaH = 2*atan( exp( (-1)* rapH ) );
		rapC = CCand_cms.PseudoRapidity();
                thetaC = 2*atan( exp( (-1)* rapC ) );
		theta = thetaH - thetaC;
*/
//	return cos( theta );
	return HCand_cms.CosTheta();
}
double costhetatb(double ptsj1Tagged, double etasj1Tagged, double phisj1Tagged, double Msj1Tagged, double CSVsj1Tagged, double ptsj2Tagged, double etasj2Tagged, double phisj2Tagged, double Msj2Tagged, double CSVsj2Tagged)
{

	 TLorentzVector sj1Cand, sj2Cand, CCand, sj1Cand_cms, sj2Cand_cms, CCand_cms;
	 TVector3 CCand_Boost;
	 double rapsj2,thetasj2, rapC, thetaC, theta;

                sj1Cand.SetPtEtaPhiM(ptsj1Tagged,
                         etasj1Tagged,
                         phisj1Tagged,
                         Msj1Tagged);

                sj2Cand.SetPtEtaPhiM(ptsj2Tagged,
                         etasj2Tagged,
                         phisj2Tagged,
                         Msj2Tagged);
	
		CCand = sj1Cand + sj2Cand;

		CCand_Boost  = CCand.BoostVector();

          if (CSVsj1Tagged>CSVsj2Tagged){
                sj1Cand_cms = sj1Cand;
                sj1Cand_cms.Boost( -1 * CCand_Boost);
                return sj1Cand_cms.CosTheta();
          }
          else if (CSVsj2Tagged > CSVsj1Tagged){
   		sj2Cand_cms = sj2Cand;
   		sj2Cand_cms.Boost( -1 * CCand_Boost);
                return sj2Cand_cms.CosTheta();
          }
          return 1.;
}

double costhetatbInv(double ptsj1Tagged, double etasj1Tagged, double phisj1Tagged, double Msj1Tagged, double CSVsj1Tagged, double ptsj2Tagged, double etasj2Tagged, double phisj2Tagged, double Msj2Tagged, double CSVsj2Tagged)
{

	 TLorentzVector sj1Cand, sj2Cand, CCand, sj1Cand_cms, sj2Cand_cms, CCand_cms;
	 TVector3 CCand_Boost;
	 double rapsj2,thetasj2, rapC, thetaC, theta;

                sj1Cand.SetPtEtaPhiM(ptsj1Tagged,
                         etasj1Tagged,
                         phisj1Tagged,
                         Msj1Tagged);

                sj2Cand.SetPtEtaPhiM(ptsj2Tagged,
                         etasj2Tagged,
                         phisj2Tagged,
                         Msj2Tagged);
	
		CCand = sj1Cand + sj2Cand;

		CCand_Boost  = CCand.BoostVector();

          if (CSVsj1Tagged>CSVsj2Tagged){
                sj1Cand_cms = sj1Cand;
                sj1Cand_cms.Boost( -1 * CCand_Boost);
                return sj2Cand_cms.CosTheta();
          }
          else if (CSVsj2Tagged > CSVsj1Tagged){
   		sj2Cand_cms = sj2Cand;
   		sj2Cand_cms.Boost( -1 * CCand_Boost);
                return sj1Cand_cms.CosTheta();
          }
          return 1.;
}
double gammabeta(double ptTopTagged, double etaTopTagged, double phiTopTagged, double MTopTagged, double ptHTagged, double etaHTagged, double phiHTagged, double MHTagged)
{

 	TLorentzVector TCand, HCand;
 	double Ph, Pt;

                TCand.SetPtEtaPhiM(ptTopTagged,
                         etaTopTagged,
                         phiTopTagged,
                         MTopTagged);

                HCand.SetPtEtaPhiM(ptHTagged,
                         etaHTagged,
                         phiHTagged,
                         MHTagged);

 //      	Ph = sqrt( (HCand.Px())*(HCand.Px()) + (HCand.Py())*(HCand.Py()) + (HCand.Pz())*(HCand.Pz()) );
 //             Pt = sqrt( (TCand.Px())*(TCand.Px()) + (TCand.Py())*(TCand.Py()) + (TCand.Pz())*(TCand.Pz()) );

	return ((HCand + TCand).Gamma())*((HCand + TCand).Beta());
//      return abs((HCand + TCand).Pt() )/mtprime;
//	return (Ph + Pt)/mtprime; 
}
