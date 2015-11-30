import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1000v2/151103_224909/0000/PreselEvents_QCDHT1000v2_1.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1000v2/151103_224909/0000/PreselEvents_QCDHT1000v2_2.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1000v2/151120_044350/0000/PreselEvents_QCDHT1000v2_3.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1000v2/151103_224909/0000/PreselEvents_QCDHT1000v2_4.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1000v2/151103_224909/0000/PreselEvents_QCDHT1000v2_5.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT1000to1500_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT1000v2/151103_224909/0000/PreselEvents_QCDHT1000v2_6.root',
    )
)

