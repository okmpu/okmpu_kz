from rest_framework import serializers
from .models import Section, Subsection


# Section
# ----------------------------------------------------------------------------------------------------------------------
class SectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        exclude = ('name', 'index', )


# Subsection
# ----------------------------------------------------------------------------------------------------------------------
class SectionExtendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'slug', )


class SubsectionListSerializer(serializers.ModelSerializer):
    section = SectionExtendSerializer(read_only=True)

    class Meta:
        model = Subsection
        fields = ('id', 'name_kk', 'name_ru', 'name_en', 'section', 'slug', )
