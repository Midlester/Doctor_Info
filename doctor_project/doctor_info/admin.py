from django.contrib import admin # type: ignore
from .models import DoctorInfo
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.formats.base_formats import XLSX

# Register your models here.

class DoctorInfoResource(resources.ModelResource):
    class Meta:
        model = DoctorInfo
        fields = ('id', 'sl', 'dls_id', 'aci_id', 'name', 'divisions', 'district', 'upazilla', 'union', 'photo')

class DoctorInfoAdmin(ImportExportModelAdmin):
    resource_class = DoctorInfoResource
    list_display = ('sl', 'dls_id', 'aci_id', 'name', 'divisions', 'district', 'upazilla', 'union')
    search_fields = ('name', 'dls_id', 'aci_id', 'divisions', 'district', 'upazilla', 'union')
    # Do NOT override get_export_formats or get_import_formats. Let import-export auto-detect formats.

admin.site.register(DoctorInfo, DoctorInfoAdmin)