# Knowledge Acquisition — Books, Articles, Documents
## Sources and artifact formats
PDF, EPUB, HTML articles, DOCX, TXT, RSS metadata, open reports, images/audio/video when approved. Catalog separately from legally stored fulltext.
## Catalog metadata
work_id; title; author/publisher (published names only); publication/edition; language; ISBN/DOI/URL as relevant; license/permission; source_uri; acquired_at; publication_at; format; SHA-256 where stored; parse_version; topic; keywords; classification; confidence; duplicate_group; review_state; references.
## Workflow
Discovery → access/license validation → capture bibliographic metadata → decide metadata-only / fulltext permitted → integrity hash → antivirus/file isolation → text extraction → language/structure detection → OCR selectively → chapters/sections references → semantic chunks with page span → embeddings/RAG → analyst review → ingestion to knowledge base.
## Distinct storage
Raw authorized artifact; catalog record; extracted searchable text; controlled vector index; interpretations/claims; source citation. Every indexed statement traces to section and version.
## Quality
OCR quality, text extraction coverage, dedup precision, known revisions, bibliographic completeness, citation resolution, licensed retention, rejection reason, correction workflow.
## Non-goals
Copyright-infringing bulk downloading, bypass of access controls, unrestricted public redistribution. Public repo never stores copyrighted full texts or personal case data.
