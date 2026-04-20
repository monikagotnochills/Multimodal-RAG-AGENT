import operator
from typing import Annotated, Dict, List, Optional, Any, TypedDict


# DEFINE THE SCHEMA FOR A SIMPLE COMPLIANCE RESULT


# error report
class ComplianceIssue(TypedDict):
    category: str
    description: str  # SPECIFIC DETAIL OF VIOLATION
    severity: str  # CRITICAL/WARNING
    timestamp: Optional[str]


# define the global graph state
# THIS DEFINES THE STATE THAT GETS PASSED AROUND IN THE AGENTIC WORKFLOW
class VideoAuditState(TypedDict):
    '''
    Defines the data schema for langgraph execution content 
    main conTainer : HOLDS ALL THE INFO ABOUT THE AUDITS RIGHT FROM INITIAL URL TO THE FINAL REPORTS 
    url to final report 
    '''

    # input parameters
    video_url: str
    video_id: str

    # ingestion and extractiom data
    local_fiel_path: Optional[str]
    Video_metadata: Dict[str, Any]
    transcript: Optional[str]  # fully extracted speed to text
    ocr_text: List[str]

    # analysis output
    compliance_results: Annotated[List[ComplianceIssue], operator.add]

    # final deliverables:
    final_status: str  # PASS/FAIL
    final_report: str  # markdown FORMAT

    # SYSTEM OBSERVAILABITY PART
    # ERRORS : API TIMEOUTS , SYSTEM LEVEL ERRORS
    # SYSTEM LEVEL CRASHESLOCK
    errors: Annotated[List[str], operator.add]
