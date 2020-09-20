from unittest import TestCase

from castervoice.lib.merge.ccrmerging2.transformers.text_replacer.tr_parser import TRParser


class TestTRParser(TestCase):

    def test_parse_lines_any(self):
        """
        Tests that ANY types make it into their correct categories
        """
        parser = TRParser()
        lines = ["<<<ANY>>>",
                 "slap -> earthquake"]
        definitions = parser._parse_lines(lines)
        self.assertEqual(definitions.specs["slap"], "earthquake")
        self.assertEqual(1, len(definitions.specs))
        self.assertEqual(definitions.extras["slap"], "earthquake")
        self.assertEqual(1, len(definitions.extras))
        self.assertEqual(definitions.defaults["slap"], "earthquake")
        self.assertEqual(1, len(definitions.defaults))

    def test_parse_lines_comments(self):
        """
        Tests that partially commented lines work and that fully commented lines are excluded
        """
        parser = TRParser()
        lines = ["<<<SPEC>>>",
                 "#this line -> doesn't get in",
                 "slap -> earthquake # but this line does"]
        definitions = parser._parse_lines(lines)
        self.assertEqual(definitions.specs["slap"], "earthquake")
        self.assertEqual(1, len(definitions.specs))

    def test_parse_lines(self):
        """
        Tests that SPEC, EXTRA, DEFAULT types make it into their correct categories
        """
        parser = TRParser()
        lines = ["<<<SPEC>>>",
                 "slap -> earthquake",
                 "<<<EXTRA>>>",
                 " ",  # blank lines should not cause problems
                 "goof -> gas",
                 "<<<DEFAULT>>>",
                 "some -> none"]
        definitions = parser._parse_lines(lines)
        self.assertEqual(definitions.specs["slap"], "earthquake")
        self.assertEqual(1, len(definitions.specs))
        self.assertEqual(definitions.extras["goof"], "gas")
        self.assertEqual(1, len(definitions.extras))
        self.assertEqual(definitions.defaults["some"], "none")
        self.assertEqual(1, len(definitions.defaults))

    def test_parse_lines_not_specs(self):
        """
        Tests that NOT_SPECS types make it into their correct categories.
        """
        parser = TRParser()
        lines = ["<<<NOT_SPECS>>>",
                 "aardvark -> beta fish"]
        definitions = parser._parse_lines(lines)
        self.assertEqual(0, len(definitions.specs))
        self.assertEqual(definitions.extras["aardvark"], "beta fish")
        self.assertEqual(1, len(definitions.extras))
        self.assertEqual(definitions.defaults["aardvark"], "beta fish")
        self.assertEqual(1, len(definitions.defaults))
