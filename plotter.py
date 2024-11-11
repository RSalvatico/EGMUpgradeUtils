import uproot
from coffea.nanoevents import NanoEventsFactory
import awkward as ak
import numpy as np
import matplotlib.pyplot as plt
import mplhep

mplhep.style.use(mplhep.style.CMS)

nanofiles = ["root://cms-xrd-global.cern.ch//store/data/Run2024C/EGamma0/NANOAOD/2024ECALRATIO_JMENano-v4/2520000/13306697-4ece-4a79-b78d-4c17511af5b7.root","\
root://cms-xrd-global.cern.ch//store/data/Run2024F/EGamma0/NANOAOD/ECAL_CC_HCAL_DI_JMENano-v3/120000/008c4bf8-d369-4e8c-b806-6b19e3cc7635.root"]

ratioevents = NanoEventsFactory.from_root(nanofiles[0]).events()
ccevents    = NanoEventsFactory.from_root(nanofiles[1]).events()

event_cut = ak.all(ratioevents.Photon.mvaID_WP80 == 1, axis = 1)

fig, ax = plt.subplots()
ax.set_xlabel(r'Photon R9')
ax.hist(ak.flatten(ratioevents[event_cut].Photon.r9), bins = np.linspace(0, 30, 1))

input()

