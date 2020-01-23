# In order for this script to work, it must be placed in a directory with
# Visual Studio Code JSON theme files. The script will generate a .xml for each
# corresponding file.
import json
import os

def main():
  for filename in os.listdir('.'):
    if filename.endswith('.json'):
      print(f'Converting {filename}')
      with open(filename) as json_file:
        try:
          convert_file(filename, json.load(json_file))
        except:
          print('[ERROR!] This file doesn\'t contain valid JSON. Check if it uses exclusively "", that it has no comments and , aren\'t used in the last element of an array')
          print('https://jsonlint.com/ is pretty good for this purpose')

def convert_file(filename, data):
  # Prepare the colors
  plain_text_color = ''
  try:
    plain_text_color = color_calculator(data['colors']['editor.foreground'])
  except:
    try:
      plain_text_color = color_calculator(data['colors']['editor.background'])
    except:
      print('[ERROR!] This file doesn\'t contain a background color')
      return
  
  background = color_calculator(data['colors']['editor.background'])
  error_color = -43691
  try:
    error_color = color_calculator(data['colors']['errorForeground'])
  except KeyError:
    print('No error color provided, using the default red')

  # Gets all the colors necessary from tokenColors
  # Unknown colors == plain_text_color
  comment_color = plain_text_color
  keyword_color = plain_text_color
  string_color = plain_text_color
  number_color = plain_text_color # Not implemented
  variable_color = plain_text_color
  brace_color = plain_text_color # Might not the best implementation
  markup_color = plain_text_color # Likely not the best implementation

  i = 0 # Counts the number of parameters filled in orde to stop the loop faster
  for obj in data['tokenColors']:
    if i == 6:
      break

    try:
      if comment_color == plain_text_color and 'comment' in obj['scope']:
        comment_color = color_calculator(obj['settings']['foreground'])
        i += 1
    
      if keyword_color == plain_text_color and 'keyword' in obj['scope']:
        keyword_color = color_calculator(obj['settings']['foreground'])
        i += 1

      if string_color == plain_text_color and 'string' in obj['scope']:
        string_color = color_calculator(obj['settings']['foreground'])
        i += 1

      if variable_color == plain_text_color and 'variable' in obj['scope']:
        variable_color = color_calculator(obj['settings']['foreground'])
        i += 1
      
      if brace_color == plain_text_color and 'punctuation.definition.arguments.begin' in obj['scope']:
        brace_color = color_calculator(obj['settings']['foreground'])
        i += 1

      if markup_color == plain_text_color and 'markup.underline.link' in obj['scope']:
        markup_color = color_calculator(obj['settings']['foreground'])
        i += 1
    except KeyError:
      i += 1


  converted_content = f'''
<Item>
  <Key>{filename[:-5]}</Key>
  <Value class="java.util.ArrayList">
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-plain-style" usepfg="false" frgb="{plain_text_color}" usepbg="false" brgb="{background}" usepfont="false" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-comment-style" usepfg="false" frgb="{comment_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-keyword-style" usepfg="false" frgb="{keyword_color}" usepbg="false" brgb="{background}" usepfont="false" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-string-style" usepfg="false" frgb="{string_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-number-style" usepfg="false" frgb="{number_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-identifier-style" usepfg="false" frgb="{plain_text_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-brace-style" usepfg="false" frgb="{brace_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-operator-style" usepfg="false" frgb="{plain_text_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-markup-style" usepfg="false" frgb="{markup_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-element-style" usepfg="false" frgb="{markup_color}" usepbg="false" brgb="{background}" usepfont="false" font="1"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-attribute-name-style" usepfg="false" frgb="{markup_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-attribute-value-style" usepfg="false" frgb="{markup_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-attribute-header-style" usepfg="false" frgb="{markup_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-attribute-addition-style" usepfg="false" frgb="{number_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="base-attribute-removal-style" usepfg="false" frgb="{string_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="java-comment-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="java-string-style" usepfg="true" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="java-keyword-style" usepfg="true" frgb="{keyword_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="java-literals-style" usepfg="false" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="java-number-style" usepfg="true" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="java-identifier-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="java-operator-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="java-brace-style" usepfg="true" frgb="{brace_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="java-sqlj-style" usepfg="false" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="javadoc-comment-style" usepfg="false" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="javadoc-tag-text-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="javadoc-tag-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="false" font="1"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="html-comment-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="html-symbol-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="html-element-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="1"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="html-attribute-name-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="html-attribute-value-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-comment-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-at-rule-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="false" font="3"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-selector-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="1"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-property-style" usepfg="false" frgb="{markup_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-error-style" usepfg="false" frgb="{error_color}" usepbg="true" brgb="{background}" usepfont="false" font="2"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-identifier-style" usepfg="false" frgb="{markup_color}" usepbg="true" brgb="{background}" usepfont="false" font="1"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-unit-style" usepfg="true" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-string-style" usepfg="true" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-function-style" usepfg="false" frgb="{keyword_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-important-style" usepfg="false" frgb="{markup_color}" usepbg="true" brgb="{background}" usepfont="false" font="1"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-medium-style" usepfg="false" frgb="{markup_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="css-uri-style" usepfg="false" frgb="{markup_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-comment-style" usepfg="false" frgb="{comment_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-string-style" usepfg="false" frgb="{string_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-keyword-style" usepfg="false" frgb="{keyword_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-identifier-style" usepfg="false" frgb="{plain_text_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-number-style" usepfg="false" frgb="{number_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-brace-style" usepfg="false" frgb="{brace_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-operator-style" usepfg="false" frgb="{brace_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="properties-comment-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="properties-name-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="properties-value-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="idl-comment-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="idl-string-style" usepfg="true" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="idl-keyword-style" usepfg="true" frgb="{keyword_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="idl-identifier-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="idl-number-style" usepfg="true" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="idl-brace-style" usepfg="true" frgb="{brace_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="idl-operator-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="c++-comment-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="c++-string-style" usepfg="true" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="c++-keyword-style" usepfg="true" frgb="{keyword_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="c++-identifier-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="c++-number-style" usepfg="true" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="c++-brace-style" usepfg="true" frgb="{brace_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="c++-operator-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="diff-header-style" usepfg="true" frgb="{markup_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="diff-addition-style" usepfg="true" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="diff-removal-style" usepfg="true" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-macros-style" usepfg="true" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="PlSqlColTabAlases" usepfg="false" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="PlSqlLogger" usepfg="false" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xml-comment-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xml-document-type-style" usepfg="false" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xml-cdata-style" usepfg="false" frgb="{string_color}" usepbg="false" brgb="{background}" usepfont="false" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xml-text-style" usepfg="false" frgb="{string_color}" usepbg="false" brgb="{background}" usepfont="false" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xml-processing-instruction-style" usepfg="false" frgb="{markup_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xml-symbol-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xml-element-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="1"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xml-attribute-name-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xml-attribute-value-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapdml-comment-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapdml-string-style" usepfg="true" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapdml-keyword-style" usepfg="true" frgb="{keyword_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapdml-identifier-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapdml-number-style" usepfg="true" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapdml-brace-style" usepfg="true" frgb="{brace_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapdml-operator-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapi-comment-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapi-string-style" usepfg="true" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapi-keyword-style" usepfg="true" frgb="{keyword_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapi-identifier-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapi-number-style" usepfg="true" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapi-brace-style" usepfg="true" frgb="{brace_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="olapi-operator-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="sparql-comment-style" usepfg="true" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="sparql-string-style" usepfg="true" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="sparql-keyword-style" usepfg="true" frgb="{keyword_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="sparql-identifier-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="sparql-number-style" usepfg="true" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="sparql-brace-style" usepfg="true" frgb="{brace_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="sparql-operator-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="sparql-bind-var-highlight-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="false" font="1"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="sparql-iri-ref-highlight-style" usepfg="false" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="sparql-lexical-error" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="hcs-comment-style" usepfg="false" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="hcs-string-style" usepfg="false" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="hcs-keyword-style" usepfg="false" frgb="{keyword_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="hcs-identifier-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="hcs-number-style" usepfg="false" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="hcs-brace-style" usepfg="true" frgb="{brace_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="hcs-operator-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="js-comment-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="js-string-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="js-keyword-style" usepfg="true" frgb="{keyword_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="js-identifier-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="js-number-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="js-brace-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="js-operator-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="js-regex-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="json-comment-style" usepfg="false" frgb="{comment_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="json-name-style" usepfg="false" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="json-value-style" usepfg="false" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="json-number-style" usepfg="false" frgb="{number_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="json-brace-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="json-constants-style" usepfg="false" frgb="{variable_color}" usepbg="true" brgb="{background}" usepfont="false" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="json-separators-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xml-declaration-style" usepfg="false" frgb="{string_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xquery-keyword-style" usepfg="true" frgb="{keyword_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xquery-comment-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xquery-variable-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xquery-string-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xquery-operator-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xquery-number-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="xquery-brace-style" usepfg="true" frgb="{plain_text_color}" usepbg="true" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-custom-style1" usepfg="false" frgb="{plain_text_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-custom-style2" usepfg="false" frgb="{plain_text_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="plsql-custom-style3" usepfg="false" frgb="{plain_text_color}" usepbg="false" brgb="{background}" usepfont="true" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Style" name="class oracle.dbtools.worksheet.editor.ClickableScriptErrorPlugin-COMP_STYLE" usepfg="false" frgb="{error_color}" usepbg="false" brgb="-1" usepfont="false" font="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="find-results-highlight" enabled="true" priority="77" usefg="true" frgb="{plain_text_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="skip-results-highlight" enabled="true" priority="78" usefg="true" frgb="-18324" usebg="true" brgb="{background}" fs="0" us="0" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="replace-results-highlight" enabled="true" priority="78" usefg="true" frgb="{brace_color}" usebg="true" brgb="{background}" fs="0" us="0" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="code-highlight" enabled="true" priority="75" usefg="true" frgb="{background}" usebg="true" brgb="-4353031" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="code-highlight-secondary" enabled="true" priority="76" usefg="true" frgb="{plain_text_color}" usebg="true" brgb="-4353031" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="brace-match1-highlight" enabled="true" priority="80" usefg="true" frgb="-4353031" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="brace-match2-highlight" enabled="true" priority="80" usefg="true" frgb="{brace_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="brace-mismatch-highlight" enabled="true" priority="80" usefg="true" frgb="-18324" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="enclosing-parens-highlight" enabled="true" priority="79" usefg="true" frgb="{brace_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="enclosing-block-highlight" enabled="true" priority="79" usefg="true" frgb="{brace_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="caret-line-highlight" enabled="true" priority="10" usefg="false" frgb="0" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="guarded-highlight" enabled="true" priority="90" usefg="false" frgb="0" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="fixed-selection-style" enabled="true" priority="30" usefg="true" frgb="{plain_text_color}" usebg="true" brgb="-12302502" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-compare-addition" enabled="true" priority="20" usefg="true" frgb="{number_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-compare-deletion" enabled="true" priority="20" usefg="true" frgb="{string_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-compare-update" enabled="true" priority="20" usefg="true" frgb="-18324" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-character-compare-addition" enabled="true" priority="100" usefg="true" frgb="{number_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-character-compare-deletion" enabled="true" priority="100" usefg="true" frgb="{string_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-character-compare-update" enabled="true" priority="100" usefg="true" frgb="-18324" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-compare-conflict" enabled="true" priority="20" usefg="true" frgb="{plain_text_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-compare-resolved" enabled="true" priority="20" usefg="true" frgb="-18324" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-compare-unchosen" enabled="true" priority="20" usefg="true" frgb="{plain_text_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-block-highlight-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="9" urgb="-4353031"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-selected-block-highlight-style" enabled="true" priority="20" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="5" urgb="-4353031"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-character-add-highlight-style" enabled="true" priority="20" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="inline-character-delete_highlight-style" enabled="true" priority="20" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="click-navigation" enabled="true" priority="70" usefg="true" frgb="{plain_text_color}" usebg="false" brgb="0" fs="0" us="0" urgb="{number_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="disabled-breakpoint" enabled="true" priority="25" usefg="true" frgb="-11470213" usebg="true" brgb="-12302502" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="enabled-breakpoint" enabled="true" priority="30" usefg="true" frgb="-11470213" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="execution-point" enabled="true" priority="40" usefg="true" frgb="{number_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="oracle.dbtools.raptor.phighlight.HighlightAddin-E" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="3" urgb="{string_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="oracle.dbtools.raptor.phighlight.HighlightAddin-W" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="3" urgb="-18324"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="oracle.dbtools.raptor.phighlight.HighlightAddin-D" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="{string_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="oracle.dbtools.raptor.phighlight.HighlightAddin-J" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="-18324"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="bookmark-style" enabled="true" priority="20" usefg="true" frgb="{number_color}" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="olapdml-error-highlight-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="{string_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="olapdml-warning-highlight-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="3" urgb="-18324"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="olapdml-fatal-highlight-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="3" urgb="{string_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="syntaxbuilder.squiggly" enabled="true" priority="2" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="{string_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="syntaxbuilder.inner_selection" enabled="true" priority="100" usefg="false" frgb="0" usebg="true" brgb="-12302502" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="sparql-error-highlight-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="{string_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="sparql-warning-highlight-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="3" urgb="-18324"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="sparql-fatal-highlight-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="3" urgb="{string_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="sparql-comment-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="0" urgb="{string_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="hcssyntaxbuilder.squiggly" enabled="true" priority="2" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="{string_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="hcssyntaxbuilder.inner_selection" enabled="true" priority="100" usefg="false" frgb="0" usebg="true" brgb="-12302502" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="highlight-selection" enabled="true" priority="100" usefg="false" frgb="0" usebg="true" brgb="-12302502" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="find-select-region" enabled="true" priority="75" usefg="false" frgb="0" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="folded-block-highlight" enabled="true" priority="99" usefg="false" frgb="0" usebg="false" brgb="0" fs="2" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="folding-fade-highlight" enabled="true" priority="100" usefg="false" frgb="0" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="todo-style" enabled="true" priority="20" usefg="true" frgb="-65281" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="tab-field" enabled="true" priority="75" usefg="false" frgb="0" usebg="true" brgb="{background}" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="template-current-field" enabled="true" priority="75" usefg="false" frgb="0" usebg="true" brgb="-4144960" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-error" enabled="true" priority="60" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="{string_color}"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-warning" enabled="true" priority="55" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="-10587"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-incomplete" enabled="false" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="0" urgb="-8355712"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-advisory" enabled="false" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="0" urgb="-8355712"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-deprecated" enabled="true" priority="54" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="10" urgb="-9211021"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-unused" enabled="true" priority="52" usefg="true" frgb="{plain_text_color}" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-todo" enabled="true" priority="52" usefg="true" frgb="{brace_color}" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-constant" enabled="true" priority="49" usefg="true" frgb="{plain_text_color}" usebg="false" brgb="0" fs="1" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-interface" enabled="false" priority="60" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-abstract-class" enabled="false" priority="60" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-class" enabled="false" priority="60" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-annotation" enabled="true" priority="60" usefg="true" frgb="{plain_text_color}" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-annotation-element" enabled="false" priority="60" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-instance-method" enabled="true" priority="60" usefg="true" frgb="{plain_text_color}" usebg="false" brgb="0" fs="1" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-static-method" enabled="true" priority="60" usefg="true" frgb="{plain_text_color}" usebg="false" brgb="0" fs="1" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-instance-field" enabled="false" priority="60" usefg="true" frgb="-16777024" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-static-field" enabled="false" priority="60" usefg="true" frgb="-16777024" usebg="false" brgb="0" fs="2" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-constructor" enabled="true" priority="60" usefg="true" frgb="-1120043" usebg="false" brgb="0" fs="1" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-parameter" enabled="false" priority="60" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="audit-variable" enabled="false" priority="60" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="java-class-separator-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="5" urgb="-4144960"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="java-member-separator-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="9" urgb="-4144960"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="oracle.jdevimpl.refactoring.highlight.HighlightControler" enabled="true" priority="75" usefg="false" frgb="0" usebg="true" brgb="-256" fs="0" us="-1" urgb="0"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="css-error-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="-65536"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="css-style-separator-style" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="5" urgb="-4144960"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="oracle.dbdev.phighlight.HighlightAddin-E" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="-65536"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="oracle.dbdev.phighlight.HighlightAddin-W" enabled="true" priority="50" usefg="false" frgb="0" usebg="false" brgb="0" fs="0" us="4" urgb="-987136"/>
    <Item class="oracle.ide.ceditor.options.S2Highlight" name="profileStyle" enabled="true" priority="20" usefg="true" frgb="-16777216" usebg="true" brgb="-14336" fs="0" us="-1" urgb="0"/>
  </Value>
</Item>
  '''

  # Write file
  f = open(f'{filename[:-5]}.xml', 'w+')
  f.write(converted_content)
  f.close()

def color_calculator(hex):
  return int(hex[1:], 16) - 16777215 - 1

if __name__ == '__main__':
  main()