"""Test manager.py and local imports."""

import pytest

from bible_alignments.burrito import AlignmentSet, Catalog, Manager, VerseData


@pytest.fixture
def sblgntbsb() -> AlignmentSet:
    """Return a AlignmentSet instance."""
    alset: AlignmentSet = Catalog().get_alignmentset(language="eng", identifier="SBLGNT-BSB-manual")
    return alset


@pytest.fixture
def mgr(sblgntbsb: AlignmentSet) -> Manager:
    """Return a Manager instance."""
    mgr: Manager = Manager(sblgntbsb)
    return mgr


class TestManager:
    """Test manager.Manager()."""

    def test_init(self, mgr: Manager) -> None:
        """Test initialization."""
        assert mgr.scheme == "BCVWP"
        assert mgr.sourcedoc.docid == "SBLGNT"
        assert mgr.targetdoc.docid == "BSB"
        assert mgr.sourceitems["n41004003001"].lemma == "ἀκούω"
        assert mgr.targetitems["410040030021"].text == "Listen"
        assert mgr.alignmentrecords["41004003.001"].asdict()["source"] == ["n41004003001", "n41004003002"]
        assert mgr.alignmentrecords["41004003.001"].meta.id == "41004003.001"
        assert mgr.alignmentrecords["41004003.001"].identifier == "41004003.001"
        vd43: VerseData = mgr["41004003"]
        assert vd43.alignments[0][0][0].lemma == "ἀκούω"
        assert vd43.get_texts() == ["“", "Listen", "!", "A", "farmer", "went", "out", "to", "sow", "his", "seed", "."]
        assert vd43.get_texts(unique=True) == [
            "“",
            "Listen",
            "!",
            "A",
            "farmer",
            "went",
            "out",
            "to",
            "sow",
            "his",
            "seed",
            ".",
        ]
        assert vd43.get_texts(typeattr="sources") == ["Ἀκούετε", "ἰδοὺ", "ἐξῆλθεν", "ὁ", "σπείρων", "σπεῖραι"]