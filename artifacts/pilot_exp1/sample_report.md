# Pilot Exp-1 Report

- Source: `/home/kimilabra/DocWorldTrace/pilot_exp1/sample_document.json`
- Total calls: `10`
- Success rate: `100.00%`
- Expectation pass rate: `100.00%`
- Retrieval pass rate: `100.00%`
- Cache pass rate: `100.00%`

## Execution Details

### overview_doc
- Action: `overview`
- Status: `success`
- Cache hit: `False`
- Check `status`: PASS

### search_revenue
- Action: `search`
- Status: `success`
- Cache hit: `False`
- Check `status`: PASS
- Check `contains_pages`: PASS

### search_revenue_cached
- Action: `search`
- Status: `success`
- Cache hit: `True`
- Check `status`: PASS
- Check `contains_pages`: PASS
- Check `cache_hit`: PASS

### read_page_2
- Action: `read_page`
- Status: `success`
- Cache hit: `False`
- Check `status`: PASS
- Check `text_contains`: PASS

### crop_table_region
- Action: `crop`
- Status: `success`
- Cache hit: `False`
- Check `status`: PASS
- Check `text_contains`: PASS

### ocr_table_region
- Action: `ocr`
- Status: `success`
- Cache hit: `False`
- Check `status`: PASS
- Check `text_contains`: PASS

### parse_table_region
- Action: `parse_table`
- Status: `success`
- Cache hit: `False`
- Check `status`: PASS
- Check `table_rows_min`: PASS

### compute_growth
- Action: `compute`
- Status: `success`
- Cache hit: `False`
- Check `status`: PASS
- Check `value_equals`: PASS

### verify_supported_claim
- Action: `verify`
- Status: `success`
- Cache hit: `False`
- Check `status`: PASS
- Check `support_label`: PASS

### detect_layout_page_2
- Action: `detect_layout`
- Status: `success`
- Cache hit: `False`
- Check `status`: PASS
- Check `text_contains`: PASS
