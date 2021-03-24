args = split(getArgument()," ");
print("Starting processing...");
//open(args[0]);
run("16-bit");
run("Despeckle");
//run("Threshold...");
setAutoThreshold("Intermodes dark");
call("ij.plugin.frame.ThresholdAdjuster.setMode", "B&W");
setOption("BlackBackground", true);
run("Convert to Mask");
print("Image threshold done...");
run("Despeckle");

print("Saving processed image...");
saveAs("Jpeg", args[0] + ".processed.jpg");

if (args[1] == "multiple") {
  print("Multiple plants...");
  //run("Invert");
  run("Analyze Particles...", "size=200-Infinity circularity=0.00-1.00 show=Outlines display clear");
  saveAs("Jpeg", args[0] + ".multiple.jpg");
  close();
  saveAs("Results", args[0] + ".csv");
}
if (args[1] == "single") {
  print("Single plant...");
  run("Create Selection");
  run("Measure");
  saveAs("Results", args[0] + ".csv");
}

if (isOpen("Results")) {
  selectWindow("Results");
  run("Close");
}
if (isOpen("Log")) {
  selectWindow("Log");
  run("Close" );
}

close("*");
print("DONE");
exit();
