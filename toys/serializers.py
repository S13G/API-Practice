from rest_framework import serializers

from toys.models import Toy


class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toy
        fields = ('id', 'name', 'description', 'release_date', 'toy_category', 'was_included_in_home')

# # first with just the normal views
# class ToySerializer(serializers.Serializer):
#     # ---- fields to be serialized ----
#     pk = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=150)
#     description = serializers.CharField(max_length=250)
#     release_date = serializers.DateTimeField()
#     toy_category = serializers.CharField(max_length=200)
#     was_included_in_home = serializers.BooleanField(required=False)
#
#     # creates and returns a new Toy instance based on the received validated data
#     def create(self, validated_data):
#         return Toy.objects.create(**validated_data)
#
#     # updates the values for the attributes of the instance with the updated attribute values retrieved from the validated data
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.release_date = validated_data.get('release_date', instance.release_date)
#         instance.toy_category = validated_data.get('toy_category', instance.toy_category)
#         instance.was_included_in_home = validated_data.get('was_included_in_home', instance.was_included_in_home)
#         instance.save()
#         return instance
