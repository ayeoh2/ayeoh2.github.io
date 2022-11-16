import aspose.words as aw

# Load the document from disk
doc = aw.Document("HTML Educational page.docx")

# Enable export of fonts
options = aw.saving.HtmlSaveOptions()
options.export_font_resources = True
  
# Save the document as HTML
doc.save("Converted.html", options)