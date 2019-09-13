
from django import template


register = template.Library()


@register.simple_tag
def get_flow_status(flow_obj):
    z=flow_obj.flowrecord_set.last()
    return z



@register.simple_tag
def get_flow_records(flow_record_obj):
    return flow_record_obj.flow.flowrecord_set.all().order_by("date")


@register.simple_tag
def get_last_step_obj(flow_record):
    all_related_flow_records = flow_record.flow.flowrecord_set.filter(step__order=flow_record.step.order-1)
    print(all_related_flow_records,"淼谦")
    print("all_related_flow_records",all_related_flow_records)
    if all_related_flow_records:

        return all_related_flow_records.last()


