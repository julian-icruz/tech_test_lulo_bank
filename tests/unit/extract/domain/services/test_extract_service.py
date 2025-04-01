import pytest
from unittest.mock import AsyncMock

from app.extract.domain.services import ExtractService
from app.extract.domain.ports import TVMazeExtractorPort


class DummyTVMazeExtractor(TVMazeExtractorPort):
    """
    Dummy implementation of TVMazeExtractorPort for testing purposes.
    """

    async def extract_schedule(self, date: str) -> list[dict]:
        return [{"show": {"name": "Dummy Show", "id": 1}}]


@pytest.mark.asyncio
async def test_get_schedule_success():
    """
    Test that ExtractService.get_schedule returns the correct schedule data.
    """
    dummy_extractor = DummyTVMazeExtractor()
    service = ExtractService(extractor_adapter=dummy_extractor)
    schedule = await service.get_schedule("2024-01-01")
    assert isinstance(schedule, list)
    assert schedule[0]["show"]["name"] == "Dummy Show"


@pytest.mark.asyncio
async def test_get_schedule_error():
    """
    Test that ExtractService.get_schedule propagates exceptions raised by the extractor.
    """
    dummy_extractor = DummyTVMazeExtractor()
    dummy_extractor.extract_schedule = AsyncMock(
        side_effect=Exception("Extraction failed")
    )
    service = ExtractService(extractor_adapter=dummy_extractor)
    with pytest.raises(Exception, match="Extraction failed"):
        await service.get_schedule("2024-01-01")


@pytest.mark.asyncio
async def test_get_schedule_empty():
    """
    Test that ExtractService.get_schedule returns an empty list when the extractor returns no data.
    """
    dummy_extractor = DummyTVMazeExtractor()
    dummy_extractor.extract_schedule = AsyncMock(return_value=[])
    service = ExtractService(extractor_adapter=dummy_extractor)
    schedule = await service.get_schedule("2024-01-01")
    assert schedule == []


@pytest.mark.asyncio
async def test_get_schedule_multiple_entries():
    """
    Test that ExtractService.get_schedule correctly handles multiple schedule entries.
    """
    dummy_extractor = DummyTVMazeExtractor()
    schedule_data = [
        {"show": {"name": "Show 1", "id": 1}},
        {"show": {"name": "Show 2", "id": 2}},
    ]
    dummy_extractor.extract_schedule = AsyncMock(return_value=schedule_data)
    service = ExtractService(extractor_adapter=dummy_extractor)
    schedule = await service.get_schedule("2024-01-01")
    assert isinstance(schedule, list)
    assert len(schedule) == 2
    assert schedule[0]["show"]["name"] == "Show 1"
    assert schedule[1]["show"]["id"] == 2
