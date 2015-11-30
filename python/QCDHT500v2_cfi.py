import FWCore.ParameterSet.Config as cms


source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_1.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_2.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_3.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_4.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_5.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_6.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_7.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_8.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_9.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_10.root',
        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_11.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_12.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_13.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_14.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_15.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_16.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_17.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_18.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_19.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_20.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_21.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_22.root',
#        'file:/mnt/hadoop/user/uscms01/pnfs/unl.edu/data4/cms/store/user/stringer/TPrime/QCD_HT500to700_TuneCUETP8M1_13TeV-madgraphMLM-pythia8/crab_QCDHT500v2/151120_044259/0000/PreselEvents_QCDHT500v2_23.root',
    )
)

