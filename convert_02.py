import aspose.words as aw

# Load the document from disk
doc = aw.Document("HTML Educational page.docx")

# Enable round-trip information
saveOptions = aw.saving.HtmlSaveOptions()
saveOptions.export_roundtrip_information = True 

# Save the document as HTML
doc.save("Document.html", saveOptions)