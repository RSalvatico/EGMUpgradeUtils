import ROOT

ROOT.EnableImplicitMT()
d = ROOT.RDataFrame("TH1Fs", "29691.204_SingleElectronPt15Eta1p7_2p7+2026D110_ticl_v5_mustache/step3_inDQM.root")

print(d.GetColumnNames()) #The branches                                                                                                                        

names = d.Take["string"]("FullName") #[branch_type](branch_name)                                                                                               

nameValues = names.GetValue()
#print(nameValues)                                                                                                                                             
#histoName = "Egamma/Electrons/Ele2HGC_All/ele10_foundHits"                                                                                                    
histoName = "HLT/EGM/Tracking/ValidationWRTOffline/hltEgammaGsfTracksPV/matches_dDz"
hPosition = -1
for e in nameValues:
    hPosition += 1
    if e == histoName: break

print("hPosition:", hPosition)

#sub = d.Filter('FullName == %s' %histoName)                                                                                                                   
#print(hPosition)                                                                                                                                              
histos = d.Take["TH1F"]("Value")
myHisto = histos.GetValue()[hPosition]

print("nEntries:", myHisto.GetEntries())
print("mean:", myHisto.GetMean())
print("RMS:", myHisto.GetRMS())

ROOT.gStyle.SetOptStat(1)
c = ROOT.TCanvas()
c.cd()
myHisto.Draw()
c.SaveAs("NumberOfTracks_ticl_mustache.pdf")

input()
