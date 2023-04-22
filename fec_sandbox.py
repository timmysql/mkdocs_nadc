from db_dal_classes import SelectFecCommittees


x = SelectFecCommittees()
committees = x.distinct_committees()
for committee in committees:
    print(committee.committee_id)