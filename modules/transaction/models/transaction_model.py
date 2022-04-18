# Native Imports
from database.database import ModelBase
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey


class ExamsProfilesAudit(ModelBase):
    __tablename__ = "tbexams_profiles_audit"

    exams_profiles_audit_id = Column(Integer, primary_key=True, index=True)
    exam_profile_id = Column(Integer, nullable=False)
    exam_profile_user = Column(Integer, nullable=False)
    exam_profile_analyzer = Column(String, nullable=False)
    exam_profile_exam = Column(String, nullable=False)
    exam_profile_crit_val_min = Column(Float, nullable=False)
    exam_profile_crit_val_max = Column(Float, nullable=True)
    exam_profile_stats = Column(Integer, nullable=False)
    exam_profile_last_modification_user_id = Column(Integer, ForeignKey('tbusers.user_id'), nullable=False)
    exam_profile_transaction_type = Column(String, nullable=False)
    exam_profile_transaction_date_time = Column(DateTime(timezone=False), nullable=False)

    def __repr__(self) -> str:
        return str({
            'exams_profiles_audit_id': self.exams_profiles_audit_id,
            'exam_profile_id': self.exam_profile_id,
            'exam_profile_user': self.exam_profile_user,
            'exam_profile_analyzer': self.exam_profile_analyzer,
            'exam_profile_exam': self.exam_profile_exam,
            'exam_profile_crit_val_min': self.exam_profile_crit_val_min,
            'exam_profile_crit_val_max': self.exam_profile_crit_val_max,
            'exam_profile_stats': self.exam_profile_stats,
            'exam_profile_last_modification_user_id': self.exam_profile_last_modification_user_id,
            'exam_profile_transaction_type': self.exam_profile_transaction_type,
            'exam_profile_transaction_date_time': self.exam_profile_transaction_date_time
        })
