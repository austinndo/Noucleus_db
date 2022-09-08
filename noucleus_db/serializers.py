from rest_framework import serializers
from .models import Gene, Guide, User


class GuideSerializer(serializers.HyperlinkedModelSerializer):
    gene = serializers.StringRelatedField(read_only=True)
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Guide
        fields = ('id', 'gene', 'user', 'sequence', 'strand',
                  'cas', 'edit_type', 'efficiency', 'percent_gc')


class GeneSerializer(serializers.HyperlinkedModelSerializer):
    gene_guides = GuideSerializer(many=True, required=False)

    class Meta:
        model = Gene
        fields = ('id', 'name', 'species', 'function',
                  'image_ref', 'gene_guides')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_guides = GuideSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'name', 'username', 'email',
                  'affiliation', 'user_guides')
