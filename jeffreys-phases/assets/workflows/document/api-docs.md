# Document: API Docs

Input variable: `include_api_docs={{include_api_docs}}`.

If `include_api_docs` is not `true`, do not generate API docs. Write a skip
report to `{{artifact_root}}/document/api-docs-report.md` explaining that API
docs were intentionally skipped and listing any source directories that would
normally be documented.

If `include_api_docs=true`, generate API documentation from source code:

1. Run the language-appropriate doc generator (`cargo doc`, `pdoc`, `typedoc`, `go doc`)
2. For handwritten sections, document: signature, parameters, return value, errors, example
3. Verify all code examples are working and tested

Write docs to the project's standard documentation directory and write the
report path to `{{artifact_root}}/document/api-docs-report.md`.
