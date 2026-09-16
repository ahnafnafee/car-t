import unittest
import xml.etree.ElementTree as ET

from simulator.abm_assay import Assay
from simulator.plotsvg import PlotSVG


class AssayPlotTests(unittest.TestCase):
    def test_assay_initial_sample_and_end_time(self):
        assay = Assay(8, 2, 0, seed=1, hours=0.013, label="A & B < C")
        result = assay.run()
        self.assertEqual(assay.series_t[0], 0)
        self.assertAlmostEqual(assay.series_t[-1], 0.78)
        self.assertEqual(result["n_tumor0"], 8)
        self.assertEqual(result["kills_total"], 0)
        self.assertEqual(result["frac_killed"], 0)
        for svg in assay.snapshots.values():
            ET.fromstring(svg)
        with self.assertRaises(RuntimeError):
            assay.run()

    def test_invalid_assay_sizes(self):
        for tumor, tcell, hours in ((0, 2, 1), (8, 0, 1), (8, 2, 0)):
            with self.assertRaises(ValueError):
                Assay(tumor, tcell, 1e5, seed=1, hours=hours)

    def test_svg_xml_and_extent(self):
        plot = PlotSVG(title="A & B < C", xlab="time < 5")
        plot.add("one & two", [(0, 1), (1, 2)], log=True)
        plot.add("other", [(0, 0), (3, 4)])
        ET.fromstring(plot.render())
        self.assertEqual(plot.xmax, 3)
        ET.fromstring(PlotSVG().render())
