from format import *

elem0 = DocstringElement(DocstringElementType.Param)
elem0.content = DocstringParam("param0", "int", "10",
                               "the description of param0, it is very long balabalabalabalabalabblalblablalblalbalblalblablalblalblabllablalabalababalalbalblalblalblallabalaba")

elem4 = DocstringElement(DocstringElementType.Param)
elem4.content = DocstringParam(param_name="param1", default_value="string",
                               description="the description of param0, it is very long balabalabalabalabalabblalblablalblalbalblalblablalblalblabllablalabalababalalbalblalblalblallabalaba")

elem1 = DocstringElement(DocstringElementType.Return)
elem1.content = DocstringReturn(
    type_name="bool", description="true for success, false for failure")

elem2 = DocstringElement(DocstringElementType.Raise)
elem2.content = DocstringRaise(
    "IOException", "it is also very long balabalbabalabalabalabalabalabalabalabalabalababalabalbaballbalblalbalblalblalbalblalblablalblalblallblalbalblalbalbalblalbla")

elem3 = DocstringElement(DocstringElementType.Note)
elem3.content = DocstringOther(
    single_description="PEP 484_ type annotations are supported. If attribute, parameter, and return types are annotated according to PEP 484_, they do not need to be included in the docstring")


docstring1 = Docstring(1, 3, 1)
docstring1.elements = [elem0, elem1, elem2, elem3, elem4]


docstring2 = Docstring(6, 8, 1)
docstring2.elements = [elem0, elem1, elem2, elem3, elem4]

file = File(input_file_name="test.py", docs_list=[
            docstring1, docstring2], target_style=DocstringStyle.Numpydoc)

file.format()