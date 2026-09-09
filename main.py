import wb_wrapper
import files_mgr

wbs = files_mgr.FilesMgr(folder_path='utests/files').wbs
combined_wb = wb_wrapper.combine_wbs(wbs)
combined_wb.save('combined_wb.xlsx')

