import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1500v2/151120_044425/0000/PreselEvents_QCDHT1500v2_1.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1500v2/151120_044425/0000/PreselEvents_QCDHT1500v2_2.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1500v2/151120_044425/0000/PreselEvents_QCDHT1500v2_3.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1500v2/151120_044425/0000/PreselEvents_QCDHT1500v2_4.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1500to2000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1500v2/151120_044425/0000/PreselEvents_QCDHT1500v2_5.root',
    )
)

