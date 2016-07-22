void weightFunctions(){
                   std::cout << "Weighting functions loaded." << endl;
                   return;
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

double WeightHT(double HT, int shift)
{

        double wt = (1+((-0.00018784)*HT + 0.2274));
        double sigErr = TMath::Sqrt(0.000079 + (4.6073/100000000000*HT*HT) + (2*HT*-5.878/100000000));
        if(HT < 1100 || HT > 2700)
                return 1;

        return wt + (shift*sigErr) ; 

}
