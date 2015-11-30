import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_1.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_2.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_3.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_4.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_5.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_6.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_7.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_8.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_9.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_10.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_11.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_12.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_13.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_14.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_15.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_16.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_17.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_18.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_20.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT700to1000_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT700/151120_044330/0000/PreselEvents_QCDHT700_19.root',
    )
)

