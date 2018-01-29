
################################################################################
# convert TAC report from .text to markdown
################################################################################

# use pandoc to convert latex thesis to doc with references
pandoc -s text_sources/TAC/3rd_TAC_report_v02.tex \
  -t markdown \
  --bibliography=bib/PhD.bib \
  -o text_sources/TAC/3rd_TAC_report_v02.md

################################################################################
# convert paralog regulation paper from .tex to markdown
################################################################################
# convert main manuscript

cat text_sources/paralog/paralogs_main_22_forSub.tex \
  | sed "s:cite{:citep{:g" \
  > text_sources/paralog/paralogs_main_22_forSub_mod.tex

# pandoc text_sources/paralog/paralogs_main_22_forSub.tex \
pandoc text_sources/paralog/paralogs_main_22_forSub_mod.tex \
  -t markdown \
  --base-header-level=2 \
  -o text_sources/paralog/paralogs_main_22_forSub.md

  # --bibliography=bib/PhD.bib \
#===============================================================================
# convert paralog SI from .tex to markdown
#===============================================================================
pandoc -s text_sources/paralog/paralogs_SI_21_forSub.tex \
  -t markdown \
  --base-header-level=2 \
  -o text_sources/paralog/paralogs_SI_21_forSub.md


#===============================================================================
# convert paralog regulation figues from .pdf to .png
#===============================================================================
for PDFFILE in figures/paralog/fig*.pdf figures/paralog/SI/*.pdf ; do
  # echo $PDFFILE
  convert -density 600 "${PDFFILE}" "${PDFFILE%.*}".png
done


################################################################################
# convert position_effect paper from .docx to markdown
################################################################################

pandoc -s text_sources/position_effect/PredictionPosEffecNonCodRearr_AJHG_CZetal_revision_70717.docx \
  --filter python/despan.py -s \
  -t markdown \
  --base-header-level=2 \
  -o text_sources/position_effect/position_effect.main.md

  # -t markdown_strict-raw_html \
  # --no-wrap \
  # --reference-links \

 # | sed -r  's|\\\[(.*)\\\]|\[\1\]|g' \
 # | sed -r  's|\\\[|\[|g' \
 # | sed -r  's:\\\[(.*)\\\]:\[\1\]:g' \
 # | sed -r  's:<span*.>.*<\span>: :g' \

# post processing:
cat text_sources/position_effect/position_effect.main.md \
 | sed -r  's:\\\[:\[:g' \
 | sed -r  's:\\\]:\]:g' \
 | sed  's:\^1-8\^:\^1-4\^:g' \
 | sed  's:\^1-14\^:\^5-14\^:g' \
 > text_sources/position_effect/position_effect.main.formated.md

# replace citations with markdown citations
python python/convert_bib.py \
  -i text_sources/position_effect/position_effect.main.formated.md \
  -o text_sources/position_effect/position_effect.main.formated.md.fix_bib.md

#-------------------------------------------------------------------------------
# convert position effect supplemntary data to markdown
#-------------------------------------------------------------------------------
pandoc -s text_sources/position_effect/Supplemental_Data_CZetal_070317_tracked_changes.docx \
  --filter python/despan.py -s \
  -t markdown \
  --base-header-level=2 \
  -o text_sources/position_effect/position_effect.SI.md

cat text_sources/position_effect/position_effect.SI.md \
 | sed -r  's:\\\[:\[:g' \
 | sed -r  's:\\\]:\]:g' \
 > text_sources/position_effect/position_effect.SI.formated.md

# python python/convert_bib.py \
#   -i text_sources/position_effect/position_effect.SI.formated.md \
#   -o text_sources/position_effect/position_effect.SI.formated.md.fix_bib.md
#

#===============================================================================
# convert position effect figues from .tif to .png
#===============================================================================
for FILE in figures/position_effect/*.tif ; do
  # echo $PDFFILE
  convert "${FILE}" "${FILE%.*}".png
done


################################################################################
# convert TAD_evolution manuscript from .docx to markdown
################################################################################

pandoc \
  --filter python/despan.py -s \
  text_sources/TAD_evolution/TAD_evolution_manuscript_v12.docx \
  -t markdown \
  --base-header-level=2 \
  -o text_sources/TAD_evolution/TAD_evolution_ms.md

python python/convert_bib_general.py \
  -i text_sources/TAD_evolution/TAD_evolution_ms.md \
  --ref_title "1.  References" \
  --intro_name "1.  Background" \
  --separater_str "," \
  -o text_sources/TAD_evolution/TAD_evolution_ms.md.fix_bib.md

#===============================================================================
# convert TAD_evolution figues from .pdf to .png
#===============================================================================
for PDFFILE in figures/TAD_evolution/fig*.pdf ; do
  # ls -lht $PDFFILE
  convert -density 600 "${PDFFILE}" "${PDFFILE%.*}".png
done

