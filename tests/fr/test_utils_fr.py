import pytest

from scripts import utils


@pytest.mark.parametrize(
    "wikicode, expected",
    [
        ("", ""),
        ("{{absol}}", "<i>(Absolument)</i>"),
        ("{{adj-indéf-avec-de}}", "<i>(Avec de)</i>"),
        ("{{agri|fr}}", "<i>(Agriculture)</i>"),
        ("{{antiq|fr}}", "<i>(Antiquité)</i>"),
        ("{{ancre|sens_sexe}}", ""),
        ("{{emploi|au passif}}", "<i>(Au passif)</i>"),
        ("{{au pluriel}}", "<i>(Au pluriel)</i>"),
        ("{{au singulier}}", "<i>(Au singulier)</i>"),
        ("{{BE|fr}}", "<i>(Belgique)</i>"),
        ("{{bioch|nocat}}", "<i>(Biochimie)</i>"),
        ("{{couleur|#B0F2B6}}", "(Code RGB #B0F2B6)"),
        ("du XX{{e}} siècle", "du XX<sup>e</sup> siècle"),
        ("{{élec|fr}}", "<i>(Électricité)</i>"),
        ("{{finan|fr}}", "<i>(Finance)</i>"),
        ("{{FR|fr}}", "<i>(France)</i>"),
        ("{{géom|fr}}", "<i>(Géométrie)</i>"),
        ("{{graphe|fr}}", "<i>(Théorie des graphes)</i>"),
        ("{{improprement|fr}}", "<i>(Usage critiqué)</i>"),
        ("{{info|fr}}", "<i>(Informatique)</i>"),
        ("{{juri|fr}}", "<i>(Droit)</i>"),
        ("{{langage SMS}} ", "<i>(Langage SMS)</i>"),
        ("{{lien|étrange|fr}}", "étrange"),
        ("{{lien|D{{e}}}}", "D<sup>e</sup>"),
        ("{{ling|fr}}", "<i>(Linguistique)</i>"),
        ("{{math|fr}}", "<i>(Mathématiques)</i>"),
        ("{{mélio|fr}}", "<i>(Mélioratif)</i>"),
        ("{{méton|fr}}", "<i>(Par métonymie)</i>"),
        ("{{métrol|nocat=1}}", "<i>(Métrologie)</i>"),
        ("{{moderne}}", "<i>(Moderne)</i>"),
        ("{{néol|fr}}", "<i>(Néologisme)</i>"),
        ("{{nombre romain|12}}", "XII"),
        ("{{nombre romain|19}}", "XIX"),
        ("{{par ext}} ou {{figuré|fr}}", "<i>(Par extension)</i> ou <i>(Figuré)</i>"),
        ("{{part}}", "<i>(En particulier)</i>"),
        ("{{pronl|fr}}", "<i>(Pronominal)</i>"),
        ("{{QC|fr}}", "<i>(Québec)</i>"),
        ("{{région}}", "<i>(Régionalisme)</i>"),
        ("{{réf}}", ""),
        ("{{siècle2|XIX}}", "XIXème"),
        (
            "{{term|Du {{nombre romain|12}}{{e}} au {{nombre romain|19}}{{e}} siècle}} Béni.",
            "<i>(Du XII<sup>e</sup> au XIX<sup>e</sup> siècle)</i> Béni.",
        ),
        (
            "{{term|Du XII{{e}} au XIX{{e}} siècle}}",
            "<i>(Du XII<sup>e</sup> au XIX<sup>e</sup> siècle)</i>",
        ),
        ("{{unités|fr}}", "<i>(Métrologie)</i>"),
    ],
)
def test_clean_template(wikicode, expected):
    assert utils.clean(wikicode) == expected
