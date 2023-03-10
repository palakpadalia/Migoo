import frappe


@frappe.whitelist()
def test():
    new_supplier = frappe.db.sql(
        '''
     
   WITH working as(
    select
        supplier,
        item_group,
        equipment_status
    from
        `tabItem`
    where
        equipment_status = 'Working'
    group by
        item_group,
        equipment_status
),
ideal as(
    select
        supplier,
        item_group,
        equipment_status
    from
        `tabItem`
    where
        equipment_status = 'Ideal'
    group by
        item_group
),
breakdown as(
    select
        supplier,
        item_group,
        equipment_status
    from
        `tabItem`
    where
        equipment_status = 'Breakdown'
    group by
        item_group
),
occupied as(
    select
        supplier,
        item_group,
        equipment_status
    from
        `tabItem`
    where
        equipment_status = 'Occupied With Migoo'
    group by
        item_group
),
free as(
    select
        supplier,
        item_group,
        equipment_status
    from
        `tabItem`
    where
        equipment_status = 'Free'
)
select
    i.supplier as 'Supplier:Link/Supplier',
    i.supplier_name as 'Supplier Name',
    ig.item_group_name as 'Item Group:Link/Item Group',
    count(working.equipment_status) as 'Working',
    count(ideal.equipment_status) as 'Ideal',
    count(breakdown.equipment_status) as 'BreakDown',
    count(occupied.equipment_status) as 'Occupied With Migoo',
    count(free.equipment_status) as 'Free'
from
    `tabItem Group` ig
    left outer JOIN `tabItem` i ON i.item_group = ig.item_group_name
    left outer JOIN working on ig.item_group_name = working.item_group
    and working.equipment_status = i.equipment_status
    and working.supplier = i.supplier
    left outer JOIN ideal on ig.item_group_name = ideal.item_group
    and ideal.supplier = i.supplier
    and ideal.equipment_status = i.equipment_status
    left outer JOIN breakdown on ig.item_group_name = breakdown.item_group
    and breakdown.supplier = i.supplier
    and breakdown.equipment_status = i.equipment_status
    left outer JOIN occupied on ig.item_group_name = occupied.item_group
    and occupied.supplier = i.supplier
    and occupied.equipment_status = i.equipment_status
    left outer JOIN free on ig.item_group_name = free.item_group
    and free.equipment_status = i.equipment_status
    and free.supplier = i.supplier
where
    ig.parent_item_group = 'All Equipment Groups'
    and equipment_for_rent=1
group by
    ig.item_group_name,
    i.supplier
              ''', as_list=True)

    print(new_supplier)

    return new_supplier
