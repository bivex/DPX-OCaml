"""Domain models for Clean Code Smell Detection in OCaml.

Defines smell categories, severities, configurable thresholds, detections, and reports.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class SmellCategory(str, Enum):
    """Clean code smell categories for OCaml static analysis."""

    FUNCTIONS = "FUNCTIONS"
    NAMING = "NAMING"
    TYPES = "TYPES"
    CONTROL_FLOW = "CONTROL_FLOW"
    MODULES = "MODULES"
    DUPLICATION = "DUPLICATION"
    STATE_AND_EFFECTS = "STATE_AND_EFFECTS"
    DEPENDENCIES = "DEPENDENCIES"
    ERROR_HANDLING = "ERROR_HANDLING"
    TESTABILITY = "TESTABILITY"
    ARCHITECTURE = "ARCHITECTURE"
    REFACTORING_SAFETY = "REFACTORING_SAFETY"


class SmellSeverity(str, Enum):
    """Severity classification of detected smells."""

    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    @property
    def rank(self) -> int:
        return {
            SmellSeverity.CRITICAL: 4,
            SmellSeverity.HIGH: 3,
            SmellSeverity.MEDIUM: 2,
            SmellSeverity.LOW: 1,
        }[self]


class SmellThresholds(BaseModel):
    """Configurable heuristics and numerical thresholds for OCaml code smell detectors."""

    # Functions
    function_lines: int = 50
    cyclomatic_complexity: int = 10
    nesting_depth: int = 4
    function_parameters: int = 5
    match_branches: int = 10
    lambda_lines: int = 15
    conditional_return_paths: int = 6

    # Naming
    single_letter_min_scope: int = 15
    non_descriptive_scope: int = 20

    # Types
    primitive_obsession_param_count: int = 3
    tuple_element_count: int = 3
    variant_constructor_count: int = 15

    # Control Flow
    nested_match_depth: int = 3
    boolean_operator_count: int = 5
    nested_if_depth: int = 3
    magic_number_min_occurrences: int = 3
    magic_string_min_occurrences: int = 3

    # Modules
    module_lines: int = 500
    exported_value_count: int = 30
    open_count: int = 10
    god_module_loc: int = 400
    god_module_types: int = 5
    god_module_functions: int = 25
    missing_interface_function_count: int = 10

    # Duplication
    duplicate_min_lines: int = 4
    duplicate_min_tokens: int = 25

    # State & Effects
    excessive_references_threshold: int = 3

    # Dependencies
    coupling_threshold: int = 10
    feature_envy_call_threshold: int = 4


class SmellDetection(BaseModel):
    """A single detected clean code smell finding with concrete evidence and refactoring guidance."""

    smell_id: str
    category: SmellCategory
    severity: SmellSeverity
    file: str
    start_line: int
    end_line: int
    symbol: str
    evidence: str
    threshold: str
    confidence: float = Field(ge=0.0, le=1.0)
    suggested_refactoring: str


class SmellReport(BaseModel):
    """Aggregated clean code smell analysis report."""

    project_path: str
    scanned_files_count: int = 0
    elapsed_seconds: float = 0.0
    thresholds: SmellThresholds = Field(default_factory=SmellThresholds)
    detections: list[SmellDetection] = Field(default_factory=list)
    category_counts: dict[str, int] = Field(default_factory=dict)
    severity_counts: dict[str, int] = Field(default_factory=dict)

    def filter_by(
        self,
        min_severity: SmellSeverity | None = None,
        category: SmellCategory | None = None,
    ) -> list[SmellDetection]:
        results = self.detections
        if min_severity:
            results = [d for d in results if d.severity.rank >= min_severity.rank]
        if category:
            results = [d for d in results if d.category == category]
        return results
